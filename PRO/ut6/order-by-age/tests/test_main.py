import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (
        [
            {'name': 'DeRozan', 'age': 33},
            {'name': 'Lonzo', 'age': 25},
            {'name': 'Beverly', 'age': 34},
            {'name': 'Dragic', 'age': 36},
            {'name': 'Williams', 'age': 21},
        ],
        [
            {'name': 'Williams', 'age': 21},
            {'name': 'Lonzo', 'age': 25},
            {'name': 'DeRozan', 'age': 33},
            {'name': 'Beverly', 'age': 34},
            {'name': 'Dragic', 'age': 36},
        ],
    ),
    (
        [
            {'name': 'Brogdon', 'age': 30},
            {'name': 'Brown', 'age': 26},
            {'name': 'Gallinari', 'age': 34},
            {'name': 'Horford', 'age': 36},
            {'name': 'Hauser', 'age': 25},
        ],
        [
            {'name': 'Hauser', 'age': 25},
            {'name': 'Brown', 'age': 26},
            {'name': 'Brogdon', 'age': 30},
            {'name': 'Gallinari', 'age': 34},
            {'name': 'Horford', 'age': 36},
        ],
    ),
]


@pytest.mark.dependency()
def test_func_exists():
    assert getattr(main, 'order_by_age', None), 'La función principal debe llamarse order_by_age'


@pytest.mark.parametrize('people, expected', testdata)
@pytest.mark.dependency(depends=['test_func_exists'])
def test_expected(people, expected):
    assert main.order_by_age(people) == expected
