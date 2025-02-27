import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (1, [0]),
    (2, [0, 1]),
    (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
    (20, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]),
]


@pytest.mark.dependency()
def test_func_exists():
    assert getattr(main, 'fibonacci', None), 'La función principal debe llamarse fibonacci'


@pytest.mark.parametrize('n, expected', testdata)
@pytest.mark.dependency(depends=['test_func_exists'])
def test_expected(n, expected):
    assert list(main.fibonacci(n)) == expected
