from __future__ import annotations

import re
import sqlite3

DB_PATH = 'tienda.db'


class EcommerceError(Exception):
    """Clase base para errores en el sistema e-commerce"""
    pass


class User:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    def __init__(self, username: str, name: str, surname: str, id: int = None):
        """Valida el username con regex:
        - Empezar con letra minúscula
        - Terminar con dígito
        - Solo letras, números y guiones bajos
        - Mínimo 8 caracteres
        """
        pattern = r'^[a-z][a-z0-9_]{6,}[0-9]$'
        if not re.match(pattern, username):
            raise EcommerceError(f'User "{username}" does not follow security rules!')
        
        self.username = username
        self.name = name
        self.surname = surname
        self.id = id

    def save(self):
        """Guarda el usuario en la base de datos"""
        self.cur.execute(
            'INSERT INTO user (username, name, surname) VALUES (?, ?, ?)',
            (self.username, self.name, self.surname)
        )
        self.con.commit()
        self.id = self.cur.lastrowid

    def update(self):
        """Actualiza el usuario en la base de datos"""
        if self.id is None:
            raise EcommerceError(f'User "{self.username}" has not been saved into DB!')
        
        self.cur.execute(
            'UPDATE user SET username=?, name=?, surname=? WHERE id=?',
            (self.username, self.name, self.surname, self.id)
        )
        self.con.commit()

    def __str__(self):
        '''Representación: "<name> <surname>"'''
        return f'{self.name} {self.surname}'

    @classmethod
    def from_id(cls, user_id: int) -> User:
        """Crea un User desde un ID"""
        res = cls.cur.execute('SELECT * FROM user WHERE id=?', (user_id,))
        user_data = res.fetchone()
        
        if not user_data:
            raise EcommerceError(f'User with id {user_id} does not exist in DB!')
        
        return User(
            user_data['username'],
            user_data['name'],
            user_data['surname'],
            user_data['id']
        )


class Product:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    def __init__(self, name: str, stock: int, price: float, id: int = None):
        """Valida que stock no sea negativo y price sea positivo"""
        if stock < 0:
            raise EcommerceError('Stock cannot be negative!')
        if price <= 0:
            raise EcommerceError('Price must be positive!')
        
        self.name = name
        self.stock = stock
        self.price = price
        self.id = id

    def save(self):
        """Guarda el producto en la base de datos"""
        self.cur.execute(
            'INSERT INTO product (name, stock, price) VALUES (?, ?, ?)',
            (self.name, self.stock, self.price)
        )
        self.con.commit()
        self.id = self.cur.lastrowid

    def update(self):
        """Actualiza el producto en la base de datos"""
        if self.id is None:
            raise EcommerceError(f'Product "{self.name}" has not been saved into DB!')
        
        self.cur.execute(
            'UPDATE product SET name=?, stock=?, price=? WHERE id=?',
            (self.name, self.stock, self.price, self.id)
        )
        self.con.commit()

    def sell(self, qty: int):
        """Vende una cantidad del producto"""
        if qty > self.stock:
            raise EcommerceError(f'Not enough stock for product "{self.name}!"')
        
        self.stock -= qty
        self.update()

    def restock(self, qty: int):
        """Repone stock del producto"""
        if qty <= 0:
            raise EcommerceError('Restock quantity must be positive!')
        
        self.stock += qty
        self.update()

    def __str__(self):
        '''Representación: "<name>"'''
        return self.name

    def __eq__(self, other):
        """Dos productos son iguales si tienen el mismo nombre"""
        if not isinstance(other, Product):
            return False
        return self.name == other.name

    @classmethod
    def from_id(cls, product_id: int) -> Product:
        """Crea un Product desde un ID"""
        res = cls.cur.execute('SELECT * FROM product WHERE id=?', (product_id,))
        product_data = res.fetchone()
        
        if not product_data:
            raise EcommerceError(f'Product with id {product_id} does not exist in DB!')
        
        return Product(
            product_data['name'],
            product_data['stock'],
            product_data['price'],
            product_data['id']
        )


class Cart:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    @classmethod
    def purchase(cls, user_id: int, product_id: int, qty: int):
        """Realiza una compra"""
        user = User.from_id(user_id)
        product = Product.from_id(product_id)
        
        if qty <= 0:
            raise EcommerceError('Purchase quantity must be positive!')
        
        product.sell(qty)
        
        cls.cur.execute(
            'INSERT INTO cart (user_id, product_id, qty) VALUES (?, ?, ?)',
            (user.id, product.id, qty)
        )
        cls.con.commit()

    @classmethod
    def clean(cls, user_id: int):
        """Limpia el carrito y devuelve el stock"""
        # Verificar que el usuario existe
        User.from_id(user_id)
        
        # Obtener items del carrito
        res = cls.cur.execute('SELECT * FROM cart WHERE user_id=?', (user_id,))
        items = res.fetchall()
        
        # Devolver stock
        for item in items:
            product = Product.from_id(item['product_id'])
            product.restock(item['qty'])
        
        # Eliminar items del carrito
        cls.cur.execute('DELETE FROM cart WHERE user_id=?', (user_id,))
        cls.con.commit()
        cls.con.close()