from __future__ import annotations

import re
import sqlite3
from datetime import datetime, timedelta
from pathlib import Path

DB_PATH = 'hotel.db'


class HotelError(Exception):
    """Clase base para errores en el sistema de hotel"""
    pass


class DatabaseCreator:
    @staticmethod
    def create(db_path: str = DB_PATH):
        """Crea la estructura de la base de datos"""
        db = Path(db_path)
        db.unlink(missing_ok=True)

        con = sqlite3.connect(db_path)
        cur = con.cursor()

        sql = """
        CREATE TABLE guest (
            id INTEGER PRIMARY KEY,
            passport TEXT UNIQUE,
            name TEXT,
            surname TEXT,
            email TEXT UNIQUE
        );

        CREATE TABLE room (
            id INTEGER PRIMARY KEY,
            number TEXT UNIQUE,
            type TEXT,
            capacity INTEGER,
            price_per_night REAL,
            available INTEGER DEFAULT 1
        );

        CREATE TABLE booking (
            id INTEGER PRIMARY KEY,
            guest_id INTEGER,
            room_id INTEGER,
            check_in_date TEXT,
            check_out_date TEXT,
            total_price REAL,
            FOREIGN KEY (guest_id) REFERENCES guest(id),
            FOREIGN KEY (room_id) REFERENCES room(id)
        );
        """

        cur.executescript(sql)
        con.commit()
        con.close()


class Guest:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    def __init__(self, passport: str, name: str, surname: str, email: str, id: int = None):
        """Valida:
        - Pasaporte: 2 letras + 6 dígitos (ej. AB123456)
        - Email: formato válido
        """
        if not re.match(r'^[A-Z]{2}\d{6}$', passport):
            raise HotelError('Invalid passport format! Must be 2 letters + 6 digits (AB123456)')
        
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            raise HotelError('Invalid email format!')
        
        self.passport = passport
        self.name = name
        self.surname = surname
        self.email = email
        self.id = id

    def save(self):
        """Guarda el huésped en la base de datos"""
        self.cur.execute(
            'INSERT INTO guest (passport, name, surname, email) VALUES (?, ?, ?, ?)',
            (self.passport, self.name, self.surname, self.email)
        )
        self.con.commit()
        self.id = self.cur.lastrowid

    def update(self):
        """Actualiza el huésped en la base de datos"""
        if self.id is None:
            raise HotelError('Guest must be saved before update!')
        
        self.cur.execute(
            'UPDATE guest SET passport=?, name=?, surname=?, email=? WHERE id=?',
            (self.passport, self.name, self.surname, self.email, self.id)
        )
        self.con.commit()

    def __str__(self):
        '''Representación: "<name> <surname> (Passport: <passport>)"'''
        return f'{self.name} {self.surname} (Passport: {self.passport})'

    @classmethod
    def from_id(cls, guest_id: int) -> Guest:
        """Crea un Guest desde un ID"""
        res = cls.cur.execute('SELECT * FROM guest WHERE id=?', (guest_id,))
        guest_data = res.fetchone()
        
        if not guest_data:
            raise HotelError(f'Guest with id {guest_id} not found!')
        
        return Guest(
            guest_data['passport'],
            guest_data['name'],
            guest_data['surname'],
            guest_data['email'],
            guest_data['id']
        )


class Room:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    ROOM_TYPES = {'single', 'double', 'suite', 'family'}

    def __init__(self, number: str, room_type: str, capacity: int, price_per_night: float, available: bool = True, id: int = None):
        """Valida:
        - Tipo de habitación debe estar en ROOM_TYPES
        - Capacidad debe ser >= 1
        - Precio debe ser positivo
        """
        if room_type.lower() not in self.ROOM_TYPES:
            raise HotelError(f'Invalid room type! Must be one of: {", ".join(self.ROOM_TYPES)}')
        
        if capacity < 1:
            raise HotelError('Capacity must be at least 1!')
        
        if price_per_night <= 0:
            raise HotelError('Price per night must be positive!')
        
        self.number = number
        self.type = room_type.lower()
        self.capacity = capacity
        self.price_per_night = price_per_night
        self.available = available
        self.id = id

    def save(self):
        """Guarda la habitación en la base de datos"""
        self.cur.execute(
            'INSERT INTO room (number, type, capacity, price_per_night, available) VALUES (?, ?, ?, ?, ?)',
            (self.number, self.type, self.capacity, self.price_per_night, int(self.available))
        )
        self.con.commit()
        self.id = self.cur.lastrowid

    def update(self):
        """Actualiza la habitación en la base de datos"""
        if self.id is None:
            raise HotelError('Room must be saved before update!')
        
        self.cur.execute(
            'UPDATE room SET number=?, type=?, capacity=?, price_per_night=?, available=? WHERE id=?',
            (self.number, self.type, self.capacity, self.price_per_night, int(self.available), self.id)
        )
        self.con.commit()

    def set_availability(self, available: bool):
        """Cambia la disponibilidad de la habitación"""
        self.available = available
        self.update()

    def __str__(self):
        '''Representación: "Room <number> (<type>, Capacity: <capacity>)"'''
        return f'Room {self.number} ({self.type}, Capacity: {self.capacity})'

    @classmethod
    def from_id(cls, room_id: int) -> Room:
        """Crea una Room desde un ID"""
        res = cls.cur.execute('SELECT * FROM room WHERE id=?', (room_id,))
        room_data = res.fetchone()
        
        if not room_data:
            raise HotelError(f'Room with id {room_id} not found!')
        
        return Room(
            room_data['number'],
            room_data['type'],
            room_data['capacity'],
            room_data['price_per_night'],
            bool(room_data['available']),
            room_data['id']
        )


class Booking:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    @classmethod
    def create_booking(cls, guest_id: int, room_id: int, check_in_date: str, nights: int):
        """Crea una reserva:
        - Verifica que la habitación esté disponible
        - Calcula el precio total
        - Actualiza disponibilidad de la habitación
        """
        guest = Guest.from_id(guest_id)
        room = Room.from_id(room_id)
        
        if not room.available:
            raise HotelError(f'Room {room.number} is not available!')
        
        # Validar fechas
        try:
            check_in = datetime.strptime(check_in_date, '%Y-%m-%d').date()
            if check_in < datetime.now().date():
                raise HotelError('Check-in date cannot be in the past!')
        except ValueError:
            raise HotelError('Invalid date format! Use YYYY-MM-DD')
        
        if nights < 1:
            raise HotelError('Must book at least one night!')
        
        check_out = (check_in + timedelta(days=nights)).strftime('%Y-%m-%d')
        total_price = room.price_per_night * nights
        
        # Crear reserva
        cls.cur.execute(
            """INSERT INTO booking 
            (guest_id, room_id, check_in_date, check_out_date, total_price) 
            VALUES (?, ?, ?, ?, ?)""",
            (guest.id, room.id, check_in_date, check_out, total_price)
        )
        
        # Marcar habitación como no disponible
        room.set_availability(False)
        
        cls.con.commit()
        return cls.cur.lastrowid

    @classmethod
    def cancel_booking(cls, booking_id: int):
        """Cancela una reserva:
        - Marca la habitación como disponible
        - Elimina la reserva
        """
        res = cls.cur.execute('SELECT * FROM booking WHERE id=?', (booking_id,))
        booking_data = res.fetchone()
        
        if not booking_data:
            raise HotelError(f'Booking with id {booking_id} not found!')
        
        # Marcar habitación como disponible
        room = Room.from_id(booking_data['room_id'])
        room.set_availability(True)
        
        # Eliminar reserva
        cls.cur.execute('DELETE FROM booking WHERE id=?', (booking_id,))
        cls.con.commit()

    @classmethod
    def get_guest_bookings(cls, guest_id: int):
        """Obtiene todas las reservas de un huésped"""
        Guest.from_id(guest_id)  # Verifica que el huésped existe
        
        res = cls.cur.execute("""
            SELECT b.id, r.number as room_number, r.type as room_type,
                   b.check_in_date, b.check_out_date, b.total_price
            FROM booking b
            JOIN room r ON b.room_id = r.id
            WHERE b.guest_id=?
            ORDER BY b.check_in_date DESC
        """, (guest_id,))
        
        return [dict(row) for row in res.fetchall()]

    @classmethod
    def get_available_rooms(cls, room_type: str = None):
        """Obtiene habitaciones disponibles, opcionalmente filtradas por tipo"""
        query = 'SELECT * FROM room WHERE available=1'
        
        if room_type:
            if room_type.lower() not in Room.ROOM_TYPES:
                raise HotelError(f'Invalid room type! Must be one of: {", ".join(Room.ROOM_TYPES)}')
            
            query += ' AND type=?'

        res = cls.cur.execute(query, (room_type.lower(),))
        return [dict(row) for row in res.fetchall()]