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
        card_number TEXT UNIQUE,
        name TEXT,
        surname TEXT,
        active INTEGER DEFAULT 1
    );

    CREATE TABLE book (
        id INTEGER PRIMARY KEY,
        isbn TEXT UNIQUE,
        title TEXT,
        author TEXT,
        available INTEGER DEFAULT 1
    );

    CREATE TABLE loan (
        id INTEGER PRIMARY KEY,
        member_id INTEGER,
        book_id INTEGER,
        loan_date TEXT DEFAULT CURRENT_DATE,
        return_date TEXT,
        FOREIGN KEY (member_id) REFERENCES member(id),
        FOREIGN KEY (book_id) REFERENCES book(id)
    );
    """

    cur.executescript(sql)
    con.commit()
    con.close()
    
class LibraryError(Exception):
    """Clase base para errores en el sistema de biblioteca"""
    pass


class Member:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    def __init__(self, card_number: str, name: str, surname: str, active: bool = True, id: int = None):
        """Valida el número de tarjeta:
        - 4 letras mayúsculas
        - 8 dígitos
        - Separados por guión
        Ejemplo: ABCD-12345678
        """
        if not re.match(r'^[A-Z]{4}-\d{8}$', card_number):
            raise LibraryError('Invalid card number format! Must be XXXX-12345678')
        
        self.card_number = card_number
        self.name = name
        self.surname = surname
        self.active = active
        self.id = id

    def save(self):
        """Guarda el miembro en la base de datos"""
        self.cur.execute(
            'INSERT INTO member (card_number, name, surname, active) VALUES (?, ?, ?, ?)',
            (self.card_number, self.name, self.surname, int(self.active))
        )
        self.con.commit()
        self.id = self.cur.lastrowid

    def update(self):
        """Actualiza el miembro en la base de datos"""
        if self.id is None:
            raise LibraryError('Member must be saved before update!')
        
        self.cur.execute(
            'UPDATE member SET card_number=?, name=?, surname=?, active=? WHERE id=?',
            (self.card_number, self.name, self.surname, int(self.active), self.id)
        )
        self.con.commit()

    def deactivate(self):
        """Desactiva el miembro"""
        if not self.active:
            raise LibraryError('Member is already inactive!')
        
        self.active = False
        self.update()

    def activate(self):
        """Activa el miembro"""
        if self.active:
            raise LibraryError('Member is already active!')
        
        self.active = True
        self.update()

    def __str__(self):
        '''Representación: "<name> <surname> (<card_number>)"'''
        return f'{self.name} {self.surname} ({self.card_number})'

    @classmethod
    def from_id(cls, member_id: int) -> Member:
        """Crea un Member desde un ID"""
        res = cls.cur.execute('SELECT * FROM member WHERE id=?', (member_id,))
        member_data = res.fetchone()
        
        if not member_data:
            raise LibraryError(f'Member with id {member_id} not found!')
        
        return Member(
            member_data['card_number'],
            member_data['name'],
            member_data['surname'],
            bool(member_data['active']),
            member_data['id']
        )


class Book:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    def __init__(self, isbn: str, title: str, author: str, available: bool = True, id: int = None):
        """Valida el ISBN:
        - Formato ISBN-13: 13 dígitos, puede tener guiones
        """
        cleaned_isbn = isbn.replace('-', '')
        if len(cleaned_isbn) != 13 or not cleaned_isbn.isdigit():
            raise LibraryError('Invalid ISBN format! Must be 13 digits')
        
        self.isbn = isbn
        self.title = title
        self.author = author
        self.available = available
        self.id = id

    def save(self):
        """Guarda el libro en la base de datos"""
        self.cur.execute(
            'INSERT INTO book (isbn, title, author, available) VALUES (?, ?, ?, ?)',
            (self.isbn, self.title, self.author, int(self.available))
        )
        self.con.commit()
        self.id = self.cur.lastrowid

    def update(self):
        """Actualiza el libro en la base de datos"""
        if self.id is None:
            raise LibraryError('Book must be saved before update!')
        
        self.cur.execute(
            'UPDATE book SET isbn=?, title=?, author=?, available=? WHERE id=?',
            (self.isbn, self.title, self.author, int(self.available), self.id)
        )
        self.con.commit()

    def __str__(self):
        '''Representación: "<title> by <author> [ISBN: <isbn>]"'''
        return f'{self.title} by {self.author} [ISBN: {self.isbn}]'

    @classmethod
    def from_id(cls, book_id: int) -> Book:
        """Crea un Book desde un ID"""
        res = cls.cur.execute('SELECT * FROM book WHERE id=?', (book_id,))
        book_data = res.fetchone()
        
        if not book_data:
            raise LibraryError(f'Book with id {book_id} not found!')
        
        return Book(
            book_data['isbn'],
            book_data['title'],
            book_data['author'],
            bool(book_data['available']),
            book_data['id']
        )


class Loan:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    LOAN_PERIOD_DAYS = 30

    @classmethod
    def borrow(cls, member_id: int, book_id: int):
        """Registra un préstamo de libro"""
        member = Member.from_id(member_id)
        book = Book.from_id(book_id)
        
        if not member.active:
            raise LibraryError('Member is not active!')
        
        if not book.available:
            raise LibraryError('Book is not available!')
        
        # Verificar si el miembro ya tiene este libro prestado
        res = cls.cur.execute(
            'SELECT * FROM loan WHERE member_id=? AND book_id=? AND return_date IS NULL',
            (member_id, book_id)
        )
        if res.fetchone():
            raise LibraryError('Member already has this book on loan!')
        
        # Marcar libro como no disponible
        book.available = False
        book.update()
        
        # Registrar préstamo
        cls.cur.execute(
            'INSERT INTO loan (member_id, book_id) VALUES (?, ?)',
            (member_id, book_id)
        )
        cls.con.commit()

    @classmethod
    def return_book(cls, loan_id: int):
        """Registra la devolución de un libro"""
        res = cls.cur.execute('SELECT * FROM loan WHERE id=? AND return_date IS NULL', (loan_id,))
        loan_data = res.fetchone()
        
        if not loan_data:
            raise LibraryError('Loan not found or already returned!')
        
        # Marcar libro como disponible
        book = Book.from_id(loan_data['book_id'])
        book.available = True
        book.update()
        
        # Registrar fecha de devolución
        cls.cur.execute(
            'UPDATE loan SET return_date=CURRENT_DATE WHERE id=?',
            (loan_id,)
        )
        cls.con.commit()

    @classmethod
    def get_overdue_loans(cls):
        """Obtiene préstamos vencidos (más de LOAN_PERIOD_DAYS días)"""
        res = cls.cur.execute("""
            SELECT * FROM loan 
            WHERE return_date IS NULL 
            AND loan_date < date('now', ?)
        """, (f'-{cls.LOAN_PERIOD_DAYS} days',))
        
        return [dict(row) for row in res.fetchall()]

    @classmethod
    def get_member_loans(cls, member_id: int):
        """Obtiene todos los préstamos de un miembro"""
        Member.from_id(member_id)  # Verifica que el miembro existe
        
        res = cls.cur.execute("""
            SELECT l.id, b.title, b.author, l.loan_date, l.return_date 
            FROM loan l
            JOIN book b ON l.book_id = b.id
            WHERE l.member_id=?
            ORDER BY l.loan_date DESC
        """, (member_id,))
        
        return [dict(row) for row in res.fetchall()]