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

# ************************************************************
# Usuario
# ************************************************************


class User:
    
    # Conexión (modo fila para la factoría) y cursor como atributos de clase
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    def __init__(self, username: str, name: str, surname: str, id: int = None):
        '''Comprueba que el username siga el siguiente patrón (usando regex):
        - Empezar con una letra minúscula.
        - Terminar con un dígito.
        - Estar formado por letras, números y guiones bajos.
        - Tener un mínimo de 8 caracteres.
        Si no sigue este patrón, hay que elevar una excepción ValueError con el
        mensaje: User "<username>" does not follow security rules!

        A continuación guarda los atributos pasados por parámetro.'''
        # Expresión regular para validar el username
        pattern = r'^[a-z][a-z0-9_]{6,}[0-9]$'
        if not re.match(pattern, username):
            raise ValueError(f'User "{username}" does not follow security rules!')
        self.username = username
        self.name = name
        self.surname = surname
        self.id = id

    def save(self):
        """Almacena el objeto actual en la base de datos y actualiza el
        identificador del objeto desde la base de datos."""
        # Insertar el usuario en la base de datos
        self.cur.execute("""
            INSERT INTO user (username, name, surname)
            VALUES (?, ?, ?)
        """, (self.username, self.name, self.surname))
        # Obtener el id del usuario recién insertado
        self.con.commit()
        self.id = self.cur.lastrowid


    def update(self):
        '''Actualiza todos los campos del objeto en la base de datos usando
        el identificador como referencia.
        Si el objeto aún no se ha guardado en la base de datos, lanza una excepción de tipo
        ValueError con el mensaje: User "<username>" has not been yet saved into DB!'''
        if self.id is None:
            raise ValueError(f'User "{self.username}" has not been yet saved into DB!')
        # Actualizar el usuario en la base de datos
        self.cur.execute("""
            UPDATE user
            SET username = ?, name = ?, surname = ?
            WHERE id = ?
        """, (self.username, self.name, self.surname, self.id))
        self.con.commit()


    def __str__(self):
        """Representación en formato:
        <name> <surname>"""
        return f'{self.name} {self.surname}'


    @classmethod
    def from_id(cls, user_id: int) -> User:
        """Construye un objeto User a partir del identificador de usuario consultando
        la base de datos.
        Si el identificador de usuario no existe hay que lanzar una excepción de tipo
        ValueError con el mensaje: User with id <user_id> does not exist in DB!"""
        # Conexión (modo fila para la factoría) y cursor como atributos de clase
        con = sqlite3.connect(DB_PATH)
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        # Consultar el usuario en la base de datos
        cur.execute("""
            SELECT * FROM user WHERE id = ?
        """, (user_id,))
        user_row = cur.fetchone()
        if user_row is None:
            raise ValueError(f'User with id {user_id} does not exist in DB!')
        # Crear el objeto User a partir de la fila obtenida
        user = User(user_row['username'], user_row['name'], user_row['surname'], user_row['id'])
        return user
    
# ************************************************************
# Producto
# ************************************************************


class Product:
    # Conexión (modo fila para la factoría) y cursor como atributos de clase
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    def __init__(self, name: str, stock: int, price: float, id: int = None):
        """Construye el objeto creando atributos a base de los parámetros."""
        self.name = name
        self.stock = stock
        self.price = price
        self.id = id


    def save(self):
        """Almacena el objeto actual en la base de datos y actualiza el
        identificador del objeto desde la base de datos."""
        # Insertar el producto en la base de datos
        self.cur.execute("""
            INSERT INTO product (name, stock, price)
            VALUES (?, ?, ?)
        """, (self.name, self.stock, self.price))
        # Obtener el id del producto recién insertado
        self.con.commit()
        self.id = self.cur.lastrowid

    def update(self):
        '''Actualiza todos los campos del objeto en la base de datos usando
        el identificador como referencia.
        Si el objeto aún no se ha guardado en la base de datos, lanza una excepción de tipo
        ValueError con el mensaje: Product "<nombre-producto>" has not been yet saved into DB!'''
        if self.id is None:
            raise ValueError(f'Product "{self.name}" has not been yet saved into DB!')
        # Actualizar el producto en la base de datos
        self.cur.execute("""
            UPDATE product
            SET name = ?, stock = ?, price = ?
            WHERE id = ?
        """, (self.name, self.stock, self.price, self.id))
        self.con.commit()


    def sell(self, qty: int) -> None:
        '''Si la cantidad a vender es mayor que el stock hay que lanzar una excepción de tipo
        ValueError con el mensaje: Not enough stock for product "<nombre-producto>!"
        Si todo ha ido bien hay que actualizar el atributo de stock del objeto y actualizar
        la información del objeto en la base de datos.'''
        if qty > self.stock:
            raise ValueError(f'Not enough stock for product "{self.name}"!')
        self.stock -= qty
        # Actualizar el stock en la base de datos
        self.cur.execute("""
            UPDATE product
            SET stock = ?
            WHERE id = ?
        """, (self.stock, self.id))
        self.con.commit()
        # Actualizar el objeto en la base de datos
        self.update()

    def restock(self, qty: int) -> None:
        """Actualiza el atributo stock del objeto según corresponda y actualiza la información
        del objeto en la base de datos.
        Haz uso de métodos ya implementados."""
        self.stock += qty
        # Actualizar el stock en la base de datos
        self.cur.execute("""
            UPDATE product
            SET stock = ?
            WHERE id = ?
        """, (self.stock, self.id))
        self.con.commit()
        # Actualizar el objeto en la base de datos
        self.update()

    def __str__(self):
        """El product se representa por su nombre."""
        return self.name
    
    def __eq__(self, other: Product | object):
        """Comprueba que dos productos son iguales únicamente a través de su nombre."""
        if isinstance(other, Product):
            return self.name == other.name
        return False

    @classmethod
    def from_id(cls, product_id: int) -> Product:
        """Construye un objeto Product a partir del identificador de producto consultando
        la base de datos.
        Si el identificador de producto no existe hay que lanzar una excepción de tipo
        ValueError con el mensaje: Product with id <product_id> does not exist in DB!"""
        # Conexión (modo fila para la factoría) y cursor como atributos de clase
        con = sqlite3.connect(DB_PATH)
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        # Consultar el producto en la base de datos
        cur.execute("""
            SELECT * FROM product WHERE id = ?
        """, (product_id,))
        product_row = cur.fetchone()
        if product_row is None:
            raise ValueError(f'Product with id {product_id} does not exist in DB!')
        # Crear el objeto Product a partir de la fila obtenida
        product = Product(product_row['name'], product_row['stock'], product_row['price'], product_row['id'])
        # Cerrar la conexión
        con.close()
        return product


# ************************************************************
# Carrito
# ************************************************************


class Cart:
    # Conexión (modo fila para la factoría) y cursor como atributos de clase
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    @classmethod
    def purchase(cls, user_id: int, product_id: int, qty: int) -> None:
        '''El usuario compra qty unidades de producto.
        Esto implica que hay que actualizar el stock del producto así como añadir
        una nueva fila en la tabla "cart" con la operación.
        Aprovecha métodos ya definidos en las clases anteriores para algunas de las
        partes que debes implementar.'''
        # Consultar el producto en la base de datos
        product = Product.from_id(product_id)
        # Consultar el usuario en la base de datos
        user = User.from_id(user_id)
        # Actualizar el stock del producto
        product.sell(qty)
        # Insertar el producto en el carrito
        cls.cur.execute("""
            INSERT INTO cart (user_id, product_id, qty)
            VALUES (?, ?, ?)
        """, (user.id, product.id, qty))
        cls.con.commit()
        # Cerrar la conexión
        cls.con.close()

    @classmethod
    def clean(cls, user_id: int) -> None:
        """Vaciar el carrito de la compra.
        Hay que actualizar el stock de los productos que había en el carrito
        así como eliminar los productos en sí mismos del carrito.
        Aprovecha métodos ya definidos en las clases anteriores para algunas de las
        partes que debes implementar."""
        # Consultar el carrito de la compra del usuario
        cls.cur.execute("""
            SELECT * FROM cart WHERE user_id = ?
        """, (user_id,))
        cart_rows = cls.cur.fetchall()
        # Actualizar el stock de los productos que había en el carrito
        for row in cart_rows:
            product = Product.from_id(row['product_id'])
            product.restock(row['qty'])
        # Eliminar los productos en sí mismos del carrito
        cls.cur.execute("""
            DELETE FROM cart WHERE user_id = ?
        """, (user_id,))
        cls.con.commit()
        # Cerrar la conexión
        cls.con.close()

