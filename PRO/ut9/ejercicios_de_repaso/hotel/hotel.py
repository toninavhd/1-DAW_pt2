from __future__ import annotations
import re
import sqlite3

DB_PATH = 'hotel.db'

def create(db_path: str):
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    sql = """
    CREATE TABLE guest (
        id INTEGER PRIMARY KEY,
        email TEXT UNIQUE,
        name TEXT,
        phone TEXT
    );

    CREATE TABLE room (
        id INTEGER PRIMARY KEY,
        number TEXT UNIQUE,
        capacity INTEGER,
        price REAL
    );

    CREATE TABLE booking (
        id INTEGER PRIMARY KEY,
        guest_id INTEGER,
        room_id INTEGER,
        check_in TEXT,
        check_out TEXT,
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

    def __init__(self, email: str, name: str, phone: str, id: int = None):
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            raise ValueError('Invalid email format!')
        self.email = email
        self.name = name
        self.phone = phone
        self.id = id

    def save(self):
        self.cur.execute(
            'INSERT INTO guest (email, name, phone) VALUES (?, ?, ?)',
            (self.email, self.name, self.phone)
        )
        self.con.commit()
        self.id = self.cur.lastrowid

    @classmethod
    def from_id(cls, guest_id: int) -> Guest:
        cls.cur.execute('SELECT * FROM guest WHERE id = ?', (guest_id,))
        row = cls.cur.fetchone()
        if not row:
            raise ValueError(f'Guest with id {guest_id} does not exist!')
        return Guest(row['email'], row['name'], row['phone'], row['id'])

class Room:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    def __init__(self, number: str, capacity: int, price: float, id: int = None):
        self.number = number
        self.capacity = capacity
        self.price = price
        self.id = id

    def save(self):
        self.cur.execute(
            'INSERT INTO room (number, capacity, price) VALUES (?, ?, ?)',
            (self.number, self.capacity, self.price)
        )
        self.con.commit()
        self.id = self.cur.lastrowid

    @classmethod
    def from_id(cls, room_id: int) -> Room:
        cls.cur.execute('SELECT * FROM room WHERE id = ?', (room_id,))
        row = cls.cur.fetchone()
        if not row:
            raise ValueError(f'Room with id {room_id} does not exist!')
        return Room(row['number'], row['capacity'], row['price'], row['id'])

class Booking:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    @classmethod
    def create(cls, guest_id: int, room_id: int, check_in: str, check_out: str):
        guest = Guest.from_id(guest_id)
        room = Room.from_id(room_id)
        cls.cur.execute(
            'INSERT INTO booking (guest_id, room_id, check_in, check_out) VALUES (?, ?, ?, ?)',
            (guest.id, room.id, check_in, check_out)
        )
        cls.con.commit()