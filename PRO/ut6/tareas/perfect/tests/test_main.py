import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (28, True),
    (496, True),
    (512, False),
    (1024, False),
    (8128, True),
]


@pytest.mark.dependency()
def test_func_exists():
    assert getattr(main, 'is_perfect', None), 'La función principal debe llamarse is_perfect'


@pytest.mark.parametrize('n, expected', testdata)
@pytest.mark.dependency(depends=['test_func_exists'])
def test_expected(n, expected):
    assert main.is_perfect(n) == expected
