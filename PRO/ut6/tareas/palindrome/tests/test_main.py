import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('ana lava lana', True),
    ('Yo dono rosas oro no doy', True),
    ('yo soy', True),
    ('La ruta natural', True),
    ('No soy un palíndromo', False),
]


@pytest.mark.dependency()
def test_func_exists():
    assert getattr(main, 'is_palindrome', None), 'La función principal debe llamarse is_palindrome'


@pytest.mark.parametrize('text, expected', testdata)
@pytest.mark.dependency(depends=['test_func_exists'])
def test_expected(text, expected):
    assert main.is_palindrome(text) == expected
