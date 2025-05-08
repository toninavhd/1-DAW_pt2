import sqlite3
from pathlib import Path
from datetime import datetime, timedelta

import create_db
import pytest
from library import Book, LibraryError, Loan, Member

TEST_DB_PATH = 'library_test.db'

# Fixtures
@pytest.fixture(autouse=True)
def setup_db():
    create_db.create(TEST_DB_PATH)
    yield
    Path(TEST_DB_PATH).unlink(missing_ok=True)

@pytest.fixture
def db_conn():
    conn = sqlite3.connect(TEST_DB_PATH)
    conn.row_factory = sqlite3.Row
    yield conn
    conn.close()

@pytest.fixture(autouse=True)
def patch_db(monkeypatch):
    for cls in [Member, Book, Loan]:
        monkeypatch.setattr(cls, 'con', sqlite3.connect(TEST_DB_PATH))
        monkeypatch.setattr(cls.con, 'row_factory', sqlite3.Row)
        monkeypatch.setattr(cls, 'cur', cls.con.cursor())

@pytest.fixture
def sample_member():
    return Member("ABCD-12345678", "John", "Doe")

@pytest.fixture
def sample_book():
    return Book("978-3161484100", "The Great Book", "Author Name")

# Tests para Member
def test_member_creation_valid(sample_member):
    assert sample_member.card_number == "ABCD-12345678"
    assert sample_member.name == "John"
    assert sample_member.surname == "Doe"
    assert sample_member.active is True
    assert sample_member.id is None

def test_member_invalid_card_number():
    with pytest.raises(LibraryError):
        Member("invalid", "John", "Doe")
    with pytest.raises(LibraryError):
        Member("1234-ABCDEFGH", "John", "Doe")
    with pytest.raises(LibraryError):
        Member("ABC-12345678", "John", "Doe")

def test_member_save(sample_member, db_conn):
    sample_member.save()
    assert sample_member.id is not None
    
    cursor = db_conn.cursor()
    cursor.execute("SELECT * FROM member WHERE id=?", (sample_member.id,))
    member_data = cursor.fetchone()
    
    assert member_data["card_number"] == sample_member.card_number
    assert member_data["name"] == sample_member.name
    assert member_data["surname"] == sample_member.surname
    assert member_data["active"] == 1

# Tests para Book
def test_book_creation_valid(sample_book):
    assert sample_book.isbn == "978-3161484100"
    assert sample_book.title == "The Great Book"
    assert sample_book.author == "Author Name"
    assert sample_book.available is True
    assert sample_book.id is None

def test_book_invalid_isbn():
    with pytest.raises(LibraryError):
        Book("1234567890", "Title", "Author")  # ISBN-10 no permitido
    with pytest.raises(LibraryError):
        Book("978-INVALID-0", "Title", "Author")

def test_book_save(sample_book, db_conn):
    sample_book.save()
    assert sample_book.id is not None
    
    cursor = db_conn.cursor()
    cursor.execute("SELECT * FROM book WHERE id=?", (sample_book.id,))
    book_data = cursor.fetchone()
    
    assert book_data["isbn"] == sample_book.isbn
    assert book_data["title"] == sample_book.title
    assert book_data["author"] == sample_book.author
    assert book_data["available"] == 1

# Tests para Loan
def test_loan_borrow(sample_member, sample_book, db_conn):
    sample_member.save()
    sample_book.save()
    
    Loan.borrow(sample_member.id, sample_book.id)
    
    # Verificar que el libro se marcó como no disponible
    updated_book = Book.from_id(sample_book.id)
    assert updated_book.available is False
    
    # Verificar que el préstamo se registró
    cursor = db_conn.cursor()
    cursor.execute('SELECT * FROM loan WHERE member_id=? AND book_id=?', 
                  (sample_member.id, sample_book.id))
    loan_data = cursor.fetchone()
    assert loan_data is not None
    assert loan_data["return_date"] is None

def test_loan_borrow_inactive_member(sample_member, sample_book):
    sample_member.save()
    sample_book.save()
    sample_member.deactivate()
    
    with pytest.raises(LibraryError):
        Loan.borrow(sample_member.id, sample_book.id)

def test_loan_return(sample_member, sample_book, db_conn):
    sample_member.save()
    sample_book.save()
    Loan.borrow(sample_member.id, sample_book.id)
    
    # Obtener el ID del préstamo
    cursor = db_conn.cursor()
    cursor.execute('SELECT id FROM loan WHERE member_id=? AND book_id=?', 
                  (sample_member.id, sample_book.id))
    loan_id = cursor.fetchone()["id"]
    
    Loan.return_book(loan_id)
    
    # Verificar que el libro está disponible
    updated_book = Book.from_id(sample_book.id)
    assert updated_book.available is True
    
    # Verificar que se registró la fecha de devolución
    cursor.execute('SELECT return_date FROM loan WHERE id=?', (loan_id,))
    assert cursor.fetchone()["return_date"] is not None