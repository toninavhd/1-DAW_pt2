import sqlite3
from pathlib import Path


def create(db_path: str):
    db = Path(db_path)
    db.unlink(missing_ok=True)

    con = sqlite3.connect(db)
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


if __name__ == '__main__':
    create('library.db')