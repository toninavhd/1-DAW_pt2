import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('El camión chocó contra el árbol', 11),
    ('WELCOME HOME', 5),
    ('Órbita Laica', 6),
    ('Programar va de pensar, no de escribir', 12),
    ('Simple es mejor que complejo', 10),
]


@pytest.mark.dependency()
def test_func_exists():
    assert getattr(main, 'count_vowels', None), 'La función principal debe llamarse count_vowels'


@pytest.mark.parametrize('text, expected', testdata)
@pytest.mark.dependency(depends=['test_func_exists'])
def test_expected(text, expected):
    assert main.count_vowels(text) == expected
