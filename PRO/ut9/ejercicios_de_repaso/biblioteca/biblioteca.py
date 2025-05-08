from __future__ import annotations
import re
import sqlite3

DB_PATH = 'library.db'

def create(db_path: str):
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    sql = """
    CREATE TABLE member (
        id INTEGER PRIMARY KEY,
        email TEXT UNIQUE,
        name TEXT,
        surname TEXT
    );

    CREATE TABLE book (
        id INTEGER PRIMARY KEY,
        title TEXT UNIQUE,
        author TEXT,
        available INTEGER
    );

    CREATE TABLE loan (
        id INTEGER PRIMARY KEY,
        member_id INTEGER,
        book_id INTEGER,
        loan_date TEXT,
        return_date TEXT,
        FOREIGN KEY (member_id) REFERENCES member(id),
        FOREIGN KEY (book_id) REFERENCES book(id)
    );
    
    """

    cur.executescript(sql)
    con.commit()
    con.close()

class Member:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    def __init__(self, email: str, name: str, surname: str, id: int = None):
        '''Valida que el email siga el patrón:
        - Debe contener un "@" y un ".".
        - No puede empezar ni terminar con "@" o ".".
        Si no es válido, lanza ValueError con el mensaje: "Invalid email format!".
        '''
        if not re.match(r'^[^@.]+@[^@.]+\.[^@.]+$', email):
            raise ValueError('Invalid email format!')
        self.email = email
        self.name = name
        self.surname = surname
        self.id = id

    def save(self):
        """Guarda el miembro en la base de datos y actualiza su ID."""
        self.cur.execute(
            'INSERT INTO member (email, name, surname) VALUES (?, ?, ?)',
            (self.email, self.name, self.surname)
        )
        self.con.commit()
        self.id = self.cur.lastrowid

    def update(self):
        """Actualiza los datos del miembro en la base de datos."""
        if self.id is None:
            raise ValueError('Member has not been saved yet!')
        self.cur.execute(
            'UPDATE member SET email = ?, name = ?, surname = ? WHERE id = ?',
            (self.email, self.name, self.surname, self.id)
        )
        self.con.commit()

    def __str__(self):
        return f'{self.name} {self.surname}'

    @classmethod
    def from_id(cls, member_id: int) -> Member:
        """Crea un Member a partir de un ID. Si no existe, lanza ValueError."""
        cls.cur.execute('SELECT * FROM member WHERE id = ?', (member_id,))
        row = cls.cur.fetchone()
        if not row:
            raise ValueError(f'Member with id {member_id} does not exist!')
        return Member(row['email'], row['name'], row['surname'], row['id'])


class Book:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    def __init__(self, title: str, author: str, available: int = 1, id: int = None):
        self.title = title
        self.author = author
        self.available = available
        self.id = id

    def save(self):
        """Guarda el libro en la base de datos y actualiza su ID."""
        self.cur.execute(
            'INSERT INTO book (title, author, available) VALUES (?, ?, ?)',
            (self.title, self.author, self.available)
        )
        self.con.commit()
        self.id = self.cur.lastrowid

    def update(self):
        """Actualiza los datos del libro en la base de datos."""
        if self.id is None:
            raise ValueError('Book has not been saved yet!')
        self.cur.execute(
            'UPDATE book SET title = ?, author = ?, available = ? WHERE id = ?',
            (self.title, self.author, self.available, self.id)
        )
        self.con.commit()

    def __str__(self):
        return self.title

    @classmethod
    def from_id(cls, book_id: int) -> Book:
        """Crea un Book a partir de un ID. Si no existe, lanza ValueError."""
        cls.cur.execute('SELECT * FROM book WHERE id = ?', (book_id,))
        row = cls.cur.fetchone()
        if not row:
            raise ValueError(f'Book with id {book_id} does not exist!')
        return Book(row['title'], row['author'], row['available'], row['id'])

class Loan:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    @classmethod
    def borrow(cls, member_id: int, book_id: int, loan_date: str) -> None:
        """Registra un préstamo de libro. Si el libro no está disponible, lanza ValueError."""
        book = Book.from_id(book_id)
        if not book.available:
            raise ValueError(f"Book '{book.title}' is not available!")
        
        member = Member.from_id(member_id)
        book.available = 0
        book.update()

        cls.cur.execute(
            'INSERT INTO loan (member_id, book_id, loan_date) VALUES (?, ?, ?)',
            (member.id, book.id, loan_date)
        )
        cls.con.commit()

    @classmethod
    def return_book(cls, loan_id: int, return_date: str) -> None:
        """Registra la devolución de un libro y lo marca como disponible."""
        cls.cur.execute('SELECT * FROM loan WHERE id = ?', (loan_id,))
        loan = cls.cur.fetchone()
        if not loan:
            raise ValueError(f'Loan with id {loan_id} does not exist!')

        book = Book.from_id(loan['book_id'])
        book.available = 1
        book.update()

        cls.cur.execute(
            'UPDATE loan SET return_date = ? WHERE id = ?',
            (return_date, loan_id)
        )
        cls.con.commit()
