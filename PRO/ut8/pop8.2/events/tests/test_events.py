import os
import sqlite3
from pathlib import Path

import pytest

if os.path.exists('solution.py'):
    from solution import Attendance, Event, User, create_db
else:
    from main import Attendance, Event, User, create_db


TEST_DB_PATH = 'events.db'

# ==============================================================================
# FIXTURES
# ==============================================================================


@pytest.fixture(autouse=True)
def create_test_database():
    try:
        create_db(TEST_DB_PATH)
        yield
    except Exception as err:
        raise err
    finally:
        Path(TEST_DB_PATH).unlink(missing_ok=True)


@pytest.fixture()
def dbcon():
    con = sqlite3.connect(TEST_DB_PATH)
    con.row_factory = sqlite3.Row
    yield con
    con.close()


@pytest.fixture(autouse=True)
def make_db_attrs_use_test_database(monkeypatch: pytest.MonkeyPatch):
    for class_ in (User, Event, Attendance):
        monkeypatch.setattr(class_, 'con', sqlite3.connect(TEST_DB_PATH))
        monkeypatch.setattr(class_.con, 'row_factory', sqlite3.Row)
        monkeypatch.setattr(class_, 'cur', class_.con.cursor())


USER1_USERNAME = 'scrowww01K'
USER1_NAME = 'Sheryl'
USER1_SURNAME = 'Crow'


@pytest.fixture
def user1():
    return User(USER1_USERNAME, USER1_NAME, USER1_SURNAME)


USER2_USERNAME = 'sspit3t3rI'
USER2_NAME = 'Sharleen'
USER2_SURNAME = 'Spiteri'


@pytest.fixture
def user2():
    return User(USER2_USERNAME, USER2_NAME, USER2_SURNAME)


EVENT1_NAME = 'Performance'
EVENT1_SEATS = 200
EVENT1_PRICE = 35.5


@pytest.fixture
def event1():
    return Event(EVENT1_NAME, EVENT1_SEATS, EVENT1_PRICE)


EVENT2_NAME = 'Festival'
EVENT2_SEATS = 1000
EVENT2_PRICE = 50.0


@pytest.fixture
def event2():
    return Event(EVENT2_NAME, EVENT2_SEATS, EVENT2_PRICE)


EVENT3_NAME = 'Exhibition'
EVENT3_SEATS = 500
EVENT3_PRICE = 20.0


@pytest.fixture
def event3():
    return Event(EVENT3_NAME, EVENT3_SEATS, EVENT3_PRICE)


# ==============================================================================
# TESTS → DATABASE
# ==============================================================================


def test_create_db(dbcon: sqlite3.Connection):
    TABLES = {
        'user': ('id', 'username', 'name', 'surname'),
        'event': ('id', 'name', 'seats', 'price'),
        'attendance': ('id', 'user_id', 'event_id', 'num_tickets'),
    }
    assert Path(TEST_DB_PATH).exists()
    cur = dbcon.cursor()
    for table, columns in TABLES.items():
        sql = "SELECT ? FROM sqlite_schema WHERE type = 'table'"
        assert cur.execute(sql, [table]).fetchone() is not None
        sql = f"PRAGMA table_info('{table}')"
        for column in columns:
            assert column in [c['name'] for c in cur.execute(sql)], (
                f'La columna {column} no aparece en la tabla {table}'
            )


# ==============================================================================
# TESTS → USER
# ==============================================================================
def test_build_user(user1: User, dbcon: sqlite3.Connection):
    assert user1.username == USER1_USERNAME
    assert user1.name == USER1_NAME
    assert user1.surname == USER1_SURNAME
    assert user1.id is None

    res = dbcon.cursor().execute('SELECT COUNT(*) FROM user')
    assert res.fetchone()[0] == 0

    user = User(USER1_USERNAME, USER1_NAME, USER1_SURNAME, 1)
    assert user.username == USER1_USERNAME
    assert user.name == USER1_NAME
    assert user.surname == USER1_SURNAME
    assert user.id == 1

    res = dbcon.execute('SELECT COUNT(*) FROM user')
    assert res.fetchone()[0] == 0


def test_build_user_fails_when_username_is_incorrect():
    for username in ('bruce', '4bruce001', 'bruce743z', 'bruce:R9Y', 'Bruce87692', 'bru8', 'bB'):
        with pytest.raises(ValueError) as err:
            User(username, '', '')
        assert str(err.value) == 'Username does not follow security rules'


def test_save_user(user1: User, dbcon: sqlite3.Connection):
    res = dbcon.cursor().execute('SELECT COUNT(*) FROM user WHERE username=?', (USER1_USERNAME,))
    assert res.fetchone()[0] == 0

    user1.save()

    res = dbcon.cursor().execute('SELECT * FROM user WHERE username=?', (USER1_USERNAME,))
    row = res.fetchone()
    assert row['username'] == user1.username
    assert row['name'] == user1.name
    assert row['surname'] == user1.surname
    assert row['id'] == 1

    with pytest.raises(sqlite3.IntegrityError) as err:
        user1.save()
    assert str(err.value) == 'UNIQUE constraint failed: user.username'


def test_update_user(user1: User, dbcon: sqlite3.Connection):
    with pytest.raises(ValueError) as err:
        user1.update()
    assert str(err.value) == 'User has not been yet saved into DB'

    user1.save()

    res = dbcon.cursor().execute('SELECT * FROM user WHERE username=?', (USER1_USERNAME,))
    row = res.fetchone()
    assert row['username'] == user1.username
    assert row['name'] == user1.name
    assert row['surname'] == user1.surname
    assert row['id'] == 1

    user1.name = 'Guido'
    user1.surname = 'Van Rossum'
    user1.update()

    res = dbcon.cursor().execute('SELECT * FROM user WHERE username=?', (USER1_USERNAME,))
    row = res.fetchone()
    assert row['name'] == 'Guido'
    assert row['surname'] == 'Van Rossum'
    assert row['id'] == 1


def test_user_representation(user1: User, user2: User):
    assert str(user1) == 'Sheryl Crow'
    assert str(user2) == 'Sharleen Spiteri'


def test_build_user_from_id(user1: User, dbcon: sqlite3.Connection):
    dbcur = dbcon.cursor()
    dbcur.execute(
        'INSERT INTO user (username, name, surname) VALUES (?, ?, ?)',
        (user1.username, user1.name, user1.surname),
    )
    dbcon.commit()
    user_id = dbcur.lastrowid

    built_user = User.build_from_id(user_id)  # type: ignore
    assert isinstance(built_user, User)
    assert built_user.username == user1.username
    assert built_user.name == user1.name
    assert built_user.surname == user1.surname
    assert built_user.id is not None


def test_build_user_from_id_fails_when_user_id_does_not_exist():
    with pytest.raises(ValueError) as err:
        User.build_from_id(0)
    assert str(err.value) == 'User does not exist in DB'


# ==============================================================================
# TESTS → EVENT
# ==============================================================================


def test_build_event(event1: Event, dbcon: sqlite3.Connection):
    assert event1.name == EVENT1_NAME
    assert event1.seats == EVENT1_SEATS
    assert event1.price == EVENT1_PRICE
    assert event1.id is None

    res = dbcon.cursor().execute('SELECT COUNT(*) FROM event')
    assert res.fetchone()[0] == 0

    event = Event(EVENT1_NAME, EVENT1_SEATS, EVENT1_PRICE, 1)
    assert event.name == EVENT1_NAME
    assert event.seats == EVENT1_SEATS
    assert event.price == EVENT1_PRICE
    assert event.id == 1

    res = dbcon.execute('SELECT COUNT(*) FROM event')
    assert res.fetchone()[0] == 0


def test_save_event(event1: Event, dbcon: sqlite3.Connection):
    res = dbcon.cursor().execute('SELECT COUNT(*) FROM event WHERE name=?', (event1.name,))
    assert res.fetchone()[0] == 0

    event1.save()

    res = dbcon.cursor().execute('SELECT * FROM event WHERE name=?', (event1.name,))
    row = res.fetchone()
    assert row['name'] == event1.name
    assert row['seats'] == event1.seats
    assert row['price'] == event1.price
    assert row['id'] == 1

    with pytest.raises(sqlite3.IntegrityError) as err:
        event1.save()
    assert str(err.value) == 'UNIQUE constraint failed: event.name'


def test_update_event(event1: Event, event2: Event, dbcon: sqlite3.Connection):
    with pytest.raises(ValueError) as err:
        event1.update()
    assert str(err.value) == 'Event has not been yet saved into DB'

    event1.save()

    res = dbcon.cursor().execute('SELECT * FROM event WHERE name=?', (EVENT1_NAME,))
    row = res.fetchone()
    assert row['name'] == event1.name
    assert row['seats'] == event1.seats
    assert row['price'] == event1.price
    assert row['id'] == 1

    event1.seats = event2.seats
    event1.price = event2.price
    event1.update()

    res = dbcon.cursor().execute('SELECT * FROM event WHERE name=?', (EVENT1_NAME,))
    row = res.fetchone()
    assert row['name'] == event1.name
    assert row['seats'] == event1.seats
    assert row['price'] == event1.price
    assert row['id'] == 1


def test_dispatch_event(event1: Event, dbcon: sqlite3.Connection):
    sql = 'INSERT INTO event (name, seats, price) VALUES (?, ?, ?)'
    dbcur = dbcon.cursor()
    dbcur.execute(sql, (event1.name, event1.seats, event1.price))
    dbcon.commit()
    event1.id = dbcur.lastrowid

    event1.dispatch(10)

    assert event1.seats == 190

    sql = 'SELECT * FROM event WHERE id=?'
    res = dbcur.execute(sql, (event1.id,))
    row = res.fetchone()
    assert row['seats'] == 190


def test_dispatch_event_fails_when_not_enough_seats(event1: Event, dbcon: sqlite3.Connection):
    sql = 'INSERT INTO event (name, seats, price) VALUES (?, ?, ?)'
    dbcur = dbcon.cursor()
    dbcur.execute(sql, (event1.name, event1.seats, event1.price))
    dbcon.commit()
    event1.id = dbcur.lastrowid

    with pytest.raises(ValueError) as err:
        event1.dispatch(2000)
    assert str(err.value) == 'Not enough free seats for event'

    sql = 'SELECT * FROM event WHERE id=?'
    res = dbcur.execute(sql, (event1.id,))
    row = res.fetchone()
    assert row['seats'] == EVENT1_SEATS


def test_expand_event(event1: Event, dbcon: sqlite3.Connection):
    sql = 'INSERT INTO event (name, seats, price) VALUES (?, ?, ?)'
    dbcur = dbcon.cursor()
    dbcur.execute(sql, (event1.name, event1.seats, event1.price))
    dbcon.commit()
    event1.id = dbcur.lastrowid

    event1.expand(50)

    assert event1.seats == 250

    sql = 'SELECT * FROM event WHERE id=?'
    res = dbcur.execute(sql, (event1.id,))
    row = res.fetchone()
    assert row['seats'] == 250


def test_event_representation(event1: Event, event2: Event):
    assert str(event1) == EVENT1_NAME
    assert str(event2) == EVENT2_NAME


def test_events_are_equal(event1: Event, event2: Event):
    event3 = event1
    event3.name = EVENT1_NAME

    assert event1 == event3
    assert event1 != event2
    assert event1 != 'event1', 'Un evento no puede ser igual a un string'


def test_build_event_from_id(event1: Event, dbcon: sqlite3.Connection):
    dbcur = dbcon.cursor()
    dbcur.execute(
        'INSERT INTO event (name, seats, price) VALUES (?, ?, ?)',
        (event1.name, event1.seats, event1.price),
    )
    dbcon.commit()
    event_id = dbcur.lastrowid

    built_event = Event.build_from_id(event_id)  # type: ignore
    assert isinstance(built_event, Event)
    assert built_event.name == event1.name
    assert built_event.seats == event1.seats
    assert built_event.price == event1.price
    assert built_event.id is not None


def test_build_event_from_id_fails_when_event_id_does_not_exist():
    with pytest.raises(ValueError) as err:
        Event.build_from_id(0)
    assert str(err.value) == 'Event does not exist in DB'


# ==============================================================================
# TESTS → ATTENDANCE
# ==============================================================================


def test_purchase(user1: User, event1: Event, dbcon: sqlite3.Connection):
    dbcur = dbcon.cursor()

    sql = 'INSERT INTO user (username, name, surname) VALUES (?, ?, ?)'
    dbcur.execute(sql, (user1.username, user1.name, user1.surname))
    dbcon.commit()
    user1.id = dbcur.lastrowid

    sql = 'INSERT INTO event (name, seats, price) VALUES (?, ?, ?)'
    dbcur.execute(sql, (event1.name, event1.seats, event1.price))
    dbcon.commit()
    event1.id = dbcur.lastrowid

    Attendance.purchase(1, 1, 5)

    sql = 'SELECT * FROM attendance WHERE user_id=? AND event_id=?'
    res = dbcur.execute(sql, (user1.id, event1.id))
    row = res.fetchone()
    assert row['num_tickets'] == 5

    sql = 'SELECT * FROM event WHERE id=?'
    res = dbcur.execute(sql, (event1.id,))
    row = res.fetchone()
    assert row['seats'] == 195


def test_cancel(user1: User, event1: Event, dbcon: sqlite3.Connection):
    dbcur = dbcon.cursor()

    sql = 'INSERT INTO user (username, name, surname) VALUES (?, ?, ?)'
    dbcur.execute(sql, (user1.username, user1.name, user1.surname))
    dbcon.commit()
    user1.id = dbcur.lastrowid

    sql = 'INSERT INTO event (name, seats, price) VALUES (?, ?, ?)'
    dbcur.execute(sql, (event1.name, event1.seats, event1.price))
    dbcon.commit()
    event1.id = dbcur.lastrowid

    sql = 'INSERT INTO attendance (user_id, event_id, num_tickets) VALUES (?, ?, ?)'
    dbcur.execute(sql, (user1.id, event1.id, 5))
    dbcon.commit()

    sql = 'UPDATE event SET seats=seats-5 WHERE id=?'
    dbcur.execute(sql, (event1.id,))
    dbcon.commit()

    Attendance.cancel(1, 1)

    sql = 'SELECT * FROM attendance WHERE user_id=? AND event_id=?'
    res = dbcur.execute(sql, (user1.id, event1.id))
    row = res.fetchone()
    assert row is None

    sql = 'SELECT * FROM event WHERE id=?'
    res = dbcur.execute(sql, (event1.id,))
    row = res.fetchone()
    assert row['seats'] == 200
