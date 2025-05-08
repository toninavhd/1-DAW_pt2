import sqlite3
from pathlib import Path
from datetime import datetime, timedelta

import pytest # type: ignore
from hotel import Booking, DatabaseCreator, Guest, HotelError, Room

TEST_DB_PATH = 'hotel_test.db'

# Fixtures
@pytest.fixture(autouse=True)
def setup_db():
    DatabaseCreator.create(TEST_DB_PATH)
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
    for cls in [Guest, Room, Booking]:
        monkeypatch.setattr(cls, 'con', sqlite3.connect(TEST_DB_PATH))
        monkeypatch.setattr(cls.con, 'row_factory', sqlite3.Row)
        monkeypatch.setattr(cls, 'cur', cls.con.cursor())

@pytest.fixture
def sample_guest():
    return Guest('AB123456', 'John', 'Doe', 'john.doe@example.com')

@pytest.fixture
def sample_room():
    return Room('101', 'double', 2, 150.0)

# Tests para DatabaseCreator
def test_database_creator():
    db_path = 'test_create.db'
    DatabaseCreator.create(db_path)
    
    # Verificar que las tablas se crearon
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = {row[0] for row in cursor.fetchall()}
    
    assert tables == {'guest', 'room', 'booking'}
    conn.close()
    Path(db_path).unlink()

# Tests para Guest
def test_guest_creation_valid(sample_guest):
    assert sample_guest.passport == 'AB123456'
    assert sample_guest.name == 'John'
    assert sample_guest.surname == 'Doe'
    assert sample_guest.email == 'john.doe@example.com'
    assert sample_guest.id is None

def test_guest_invalid_passport():
    with pytest.raises(HotelError):
        Guest('invalid', 'John', 'Doe', 'john@example.com')
    with pytest.raises(HotelError):
        Guest('A1B2C3D4', 'John', 'Doe', 'john@example.com')

def test_guest_invalid_email():
    with pytest.raises(HotelError):
        Guest('AB123456', 'John', 'Doe', 'invalid-email')

# Tests para Room
def test_room_creation_valid(sample_room):
    assert sample_room.number == '101'
    assert sample_room.type == 'double'
    assert sample_room.capacity == 2
    assert sample_room.price_per_night == 150.0
    assert sample_room.available is True
    assert sample_room.id is None

def test_room_invalid_type():
    with pytest.raises(HotelError):
        Room('101', 'invalid', 2, 150.0)

def test_room_invalid_capacity():
    with pytest.raises(HotelError):
        Room('101', 'double', 0, 150.0)

# Tests para Booking
def test_booking_create(sample_guest, sample_room, db_conn):
    sample_guest.save()
    sample_room.save()
    
    booking_id = Booking.create_booking(sample_guest.id, sample_room.id, '2023-12-01', 3)
    assert booking_id is not None
    
    # Verificar que la habitación se marcó como no disponible
    updated_room = Room.from_id(sample_room.id)
    assert updated_room.available is False
    
    # Verificar que la reserva se creó
    cursor = db_conn.cursor()
    cursor.execute('SELECT * FROM booking WHERE id=?', (booking_id,))
    booking_data = cursor.fetchone()
    
    assert booking_data is not None
    assert booking_data['guest_id'] == sample_guest.id
    assert booking_data['room_id'] == sample_room.id
    assert booking_data['check_in_date'] == '2023-12-01'
    assert booking_data['check_out_date'] == '2023-12-04'
    assert booking_data['total_price'] == 450.0

def test_booking_cancel(sample_guest, sample_room):
    sample_guest.save()
    sample_room.save()
    
    booking_id = Booking.create_booking(sample_guest.id, sample_room.id, '2023-12-01', 3)
    Booking.cancel_booking(booking_id)
    
    # Verificar que la habitación está disponible
    updated_room = Room.from_id(sample_room.id)
    assert updated_room.available is True
    
    # Verificar que la reserva se eliminó
    res = Booking.cur.execute('SELECT * FROM booking WHERE id=?', (booking_id,))
    assert res.fetchone() is None