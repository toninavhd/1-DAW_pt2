from __future__ import annotations

import re
import sqlite3

DB_PATH = ':memory:'

def create_db(db_path: str = DB_PATH) -> None:
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    sql = """CREATE TABLE user(
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    name TEXT,
    surname TEXT
    );

    CREATE TABLE event(
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    seats INTEGER,
    price REAL
    );

    CREATE TABLE attendance (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    event_id INTEGER,
    num_tickets INTEGER,
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (event_id) REFERENCES event(id)
    );
  
    """
    cur.executescript(sql)
    con.commit()
    con.close()
    


# ==============================================================================
# USUARIO
# ==============================================================================
class User:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    def __init__(self, username: str, name: str, surname: str, id: int = None):
        regexp = r'[a-z][a-zA-Z0-9_]{8,}[A-Z]' 
        if not re.fullmatch(regexp,username):
            raise ValueError('Username does not follow security rules')
        self.username = username
        self.name = name
        self.surname = surname
        self.id = id

    def save(self) -> None:
        sql = 'INSERT INTO USER (username, name, surname) VALUES (?,?,?)'
        self.cur.execute(sql,(self.username, self.name, self.surname))
        self.con.commit()
        self.id = self.cur.lastrowid

    def update(self) -> None:
        if self.id is None:
            raise ValueError('User has not been yet saved into DB')
        sql = 'UPDATE user SET username= ?, name= ?, surname= ? WHERE id = ?'
        self.cur.execute(sql,(self.username, self.name, self.surname, self.id))
        self.con.commit()

    def __str__(self):
        return f'{self.name} {self.surname}'

    @classmethod
    def build_from_id(cls, user_id: int) -> User:
        sql = 'SELECT * FROM user WHERE id= ?'
        cls.cur.execute(sql,(user_id,))
        user_row = cls.cur.fetchone()
        if user_row is None:
            raise ValueError('User does not exist in DB')
        return cls(username=user_row['username'],
                   name=user_row['name'],
                   surname=user_row['surname'])

# ==============================================================================
# EVENTO
# ==============================================================================


class Event:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    def __init__(self, name: str, seats: int, price: float, id: int = None):
        self.name = name
        self.seats = seats
        self.price = price
        self.id = id

    def save(self) -> None:
        sql = 'INSERT INTO EVENT(name, seats, price) VALUES (?,?,?)'
        self.cur.execute(sql,(self.name, self.seats, self.price))
        self.con.commit()
        self.id = self.cur.lastrowid

    def update(self) -> None:
        if self.id is None:
            raise ValueError('Event has not been yet saved into DB')
        sql = 'UPDATE event SET name= ?, seats= ?, price= ? WHERE id = ?'
        self.cur.execute(sql,(self.name, self.seats, self.price, self.id))
        self.con.commit()

    def dispatch(self, num_tickets: int) -> None:
        if num_tickets > self.seats:
            raise ValueError ('Not enough free seats for event')
        self.seats -= num_tickets
        sql = 'UPDATE event SET seats=? WHERE id=?'
        self.cur.execute(sql,(self.seats,self.id))
        self.update()
        self.con.commit()

    def expand(self, seats: int) -> None:
        self.seats += seats 
        sql = 'UPDATE event SET seats=? WHERE id=?'
        self.cur.execute(sql,(self.seats,self.id))
        self.update()
        self.con.commit()

    def __str__(self):
        return self.name

    def __eq__(self, other: Event | object):
        if isinstance(other, Event):
            return self.name == other.name

    @classmethod
    def build_from_id(cls, event_id: int) -> Event:
        sql = 'SELECT * FROM event WHERE id = ?'
        cls.cur.execute(sql,(event_id,))
        event_row = cls.cur.fetchone()
        if event_row is None:
            raise ValueError('Event does not exist in DB')
        return cls(name = event_row['name'],
                   seats = event_row['seats'],
                   price = event_row['price'])



# ==============================================================================
# ASISTENCIA
# ==============================================================================


class Attendance:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    @classmethod
    def purchase(cls, user_id: int, event_id: int, num_tickets: int) -> None:
        event = Event.build_from_id(event_id)
        event.dispatch(num_tickets)
        sql_att = 'INSERT INTO attendance(user_id, event_id, num_tikets) VALUE (?,?,?)'
        cls.cur.execute(sql_att,(user_id,event_id,num_tickets))
        sql_ev = 'UPDATE event SET seats=? WHERE id=?'        
        cls.cur.execute(sql_ev,(event.seats,event.id))
        cls.con.commit()
        cls.con.close()

    @classmethod
    def cancel(cls, user_id: int, event_id: int) -> None:
        event = Event.build_from_id(event_id)
        event.expand(event.seats)
        sql = 'DELETE FROM attendance WHERE user_id=?'    
        cls.cur.execute(sql,(user_id,))
        cls.con.commit()
        cls.con.close()
