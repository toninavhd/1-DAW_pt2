import sqlite3
from pathlib import Path

import create_db
import ecommerce
import pytest
from ecommerce import Cart, EcommerceError, Product, User

TEST_DB_PATH = 'ecommerce_test.db'

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
    for cls in [User, Product, Cart]:
        monkeypatch.setattr(cls, 'con', sqlite3.connect(TEST_DB_PATH))
        monkeypatch.setattr(cls.con, 'row_factory', sqlite3.Row)
        monkeypatch.setattr(cls, 'cur', cls.con.cursor())

@pytest.fixture
def sample_user():
    return User("validuser1", "John", "Doe")

@pytest.fixture
def sample_product():
    return Product("Laptop", 10, 999.99)

# Tests para User
def test_user_creation_valid(sample_user):
    assert sample_user.username == "validuser1"
    assert sample_user.name == "John"
    assert sample_user.surname == "Doe"
    assert sample_user.id is None

def test_user_invalid_username():
    with pytest.raises(EcommerceError):
        User("InvalidUser", "John", "Doe")
    with pytest.raises(EcommerceError):
        User("short1", "John", "Doe")
    with pytest.raises(EcommerceError):
        User("nondigit", "John", "Doe")

def test_user_save(sample_user, db_conn):
    sample_user.save()
    assert sample_user.id is not None
    
    cursor = db_conn.cursor()
    cursor.execute("SELECT * FROM user WHERE id=?", (sample_user.id,))
    user_data = cursor.fetchone()
    
    assert user_data["username"] == sample_user.username
    assert user_data["name"] == sample_user.name
    assert user_data["surname"] == sample_user.surname

def test_user_update_not_saved(sample_user):
    with pytest.raises(EcommerceError):
        sample_user.update()

# Tests para Product
def test_product_creation_valid(sample_product):
    assert sample_product.name == "Laptop"
    assert sample_product.stock == 10
    assert sample_product.price == 999.99
    assert sample_product.id is None

def test_product_invalid_stock():
    with pytest.raises(EcommerceError):
        Product("Item", -1, 10.0)

def test_product_invalid_price():
    with pytest.raises(EcommerceError):
        Product("Item", 10, 0.0)

def test_product_sell(sample_product):
    sample_product.save()
    sample_product.sell(5)
    assert sample_product.stock == 5

def test_product_sell_not_enough_stock(sample_product):
    sample_product.save()
    with pytest.raises(EcommerceError):
        sample_product.sell(15)

# Tests para Cart
def test_cart_purchase(sample_user, sample_product, db_conn):
    sample_user.save()
    sample_product.save()
    
    Cart.purchase(sample_user.id, sample_product.id, 2)
    
    cursor = db_conn.cursor()
    cursor.execute('SELECT * FROM cart WHERE user_id=?', (sample_user.id,))
    cart_item = cursor.fetchone()
    
    assert cart_item['user_id'] == sample_user.id
    assert cart_item['product_id'] == sample_product.id
    assert cart_item['qty'] == 2
    
    # Verificar que el stock se actualizó
    updated_product = Product.from_id(sample_product.id)
    assert updated_product.stock == 8

def test_cart_clean(sample_user, sample_product):
    sample_user.save()
    sample_product.save()
    initial_stock = sample_product.stock
    
    Cart.purchase(sample_user.id, sample_product.id, 3)
    Cart.clean(sample_user.id)
    
    # Verificar que el stock volvió a su valor original
    updated_product = Product.from_id(sample_product.id)
    assert updated_product.stock == initial_stock
    
    # Verificar que el carrito está vacío
    cursor = Cart.cur.execute('SELECT COUNT(*) FROM cart WHERE user_id=?', (sample_user.id,))
    assert cursor.fetchone()[0] == 0