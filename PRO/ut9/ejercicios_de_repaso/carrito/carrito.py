from __future__ import annotations

import re
import sqlite3

DB_PATH = 'ecommerce.db'

def create(db_path: str):

    con = sqlite3.connect(db_path)
    cur = con.cursor()

    sql = """
    CREATE TABLE user (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE,
        name TEXT,
        surname TEXT
    );

    CREATE TABLE product (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE,
        stock INTEGER,
        price REAL
    );

    CREATE TABLE cart (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        product_id INTEGER,
        qty INTEGER,
        FOREIGN KEY (user_id) REFERENCES user(id),
        FOREIGN KEY (product_id) REFERENCES product(id)
    );
    """
    cur.executescript(sql)
    con.commit()
    con.close()

class User:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    def __init__(self, username: str, name: str, surname: str, id: int = None):

        pattern = r'^[a-z][a-z0-9_]{6,}[0-9]$'
        if not re.match(pattern, username):
            raise ValueError(f'User "{username}" does not follow security rules!')
        self.username = username
        self.name = name
        self.surname = surname
        self.id = id

    def save(self):
        sql_insert = """
        INSERT INTO user (username, name, surname)
        VALUES (?, ?, ?)
        """
        self.cur.execute(sql_insert, (self.username, self.name, self.surname))
        self.con.commit()
        self.id = self.cur.lastrowid

    def update(self):
        sql_update = """
        UPDATE user
        SET username = ?, name = ?, surname = ?
        WHERE id = ?
        """
        if self.id is None:
            raise ValueError(f'User "{self.username}" has not been yet saved into DB!')
        self.cur.execute(sql_update, (self.username, self.name, self.surname, self.id))
        self.con.commit()

    def __str__(self):
        return f'{self.name} {self.surname}'

    @classmethod
    def from_id(cls, user_id: int) -> User:
        con = sqlite3.connect(DB_PATH)
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        sql ='SELECT * FROM user WHERE id = ?'
    
        cur.execute(sql, (user_id,))
        user_row = cur.fetchone()
        if user_row is None:
            raise ValueError(f'User with id {user_id} does not exist in DB!')
        return cls(user_row['username'], user_row['name'], user_row['surname'], user_row['id'])
    
class Product:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    def __init__(self, name: str, stock: int, price: float, id: int = None):
        self.name = name
        self.stock = stock
        self.price = price
        self.id = id

    def save(self):
        sql_insert = """
        INSERT INTO product (name, stock, price)
        VALUES (?, ?, ?)
        """
        self.cur.execute(sql_insert, (self.name, self.stock, self.price))
        self.con.commit()
        self.id = self.cur.lastrowid

    def update(self):
        sql_update = """
        UPDATE product
        SET name = ?, stock = ?, price = ?
        WHERE id = ?
        """
        if self.id is None:
            raise ValueError(f'Product "{self.name}" has not been yet saved into DB!')
        self.cur.execute(sql_update, (self.name, self.stock, self.price, self.id))
        self.con.commit()

    def sell(self, qty: int) -> None:
        sql_update = """
        UPDATE product
        SET stock = ?
        WHERE id = ?
        """
        if qty > self.stock:
            raise ValueError(f'Not enough stock for product "{self.name}"!')
        self.stock -= qty
        self.cur.execute(sql_update, (self.stock, self.id))
        self.con.commit()
        self.update()

    def restock(self, qty: int) -> None:
        sql_update = """
        UPDATE product
        SET stock = ?
        WHERE id = ?
        """
        self.stock += qty
        self.cur.execute(sql_update, (self.stock, self.id))
        self.con.commit()
        self.update()

    def __str__(self):
        return self.name
    
    def __eq__(self, other: Product | object):
        if isinstance(other, Product):
            return self.name == other.name
        return False

    @classmethod
    def from_id(cls, product_id: int) -> Product:

        con = sqlite3.connect(DB_PATH)
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        
        cur.execute("""
            SELECT * FROM product WHERE id = ?
        """, (product_id,))
        product_row = cur.fetchone()
        if product_row is None:
            raise ValueError(f'Product with id {product_id} does not exist in DB!')
        #con.close()
        return cls(product_row['name'], product_row['stock'], product_row['price'], product_row['id']) 

class Cart:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    @classmethod
    def purchase(cls, user_id: int, product_id: int, qty: int) -> None:
        sql = """
            INSERT INTO cart (user_id, product_id, qty)
            VALUES (?, ?, ?)
        """
        product = Product.from_id(product_id)
        user = User.from_id(user_id)
        product.sell(qty)
        cls.cur.execute(sql, (user.id, product.id, qty))
        cls.con.commit()
        cls.con.close()

    @classmethod
    def clean(cls, user_id: int) -> None:
        sql_prod_check = 'SELECT * FROM cart WHERE user_id = ?'
        cls.cur.execute(sql_prod_check, (user_id,))
        cart_rows = cls.cur.fetchall()

        for row in cart_rows:
            product = Product.from_id(row['product_id'])
            product.restock(row['qty'])
        sql_delete =' DELETE FROM cart WHERE user_id = ?'

        cls.cur.execute(sql_delete, (user_id,))
        cls.con.commit()
        cls.con.close()

