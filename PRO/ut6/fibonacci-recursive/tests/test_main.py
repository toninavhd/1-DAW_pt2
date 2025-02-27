import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (1, 1),
    (2, 1),
    (10, 55),
    (20, 6765),
]


@pytest.mark.dependency()
def test_func_exists():
    assert getattr(main, 'fibonacci', None), 'La función principal debe llamarse fibonacci'


@pytest.mark.parametrize('n, expected', testdata)
@pytest.mark.dependency(depends=['test_func_exists'])
def test_expected(n, expected):
    assert main.fibonacci(n) == expected
