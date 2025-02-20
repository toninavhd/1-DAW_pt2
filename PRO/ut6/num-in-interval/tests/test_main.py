import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (3, 2, 5, True),
    (10, 10, 10, True),
    (-1, -10, 10, True),
    (5, 0, 1, False),
]


@pytest.mark.dependency()
def test_func_exists():
    assert getattr(main, 'in_range', None), 'La función principal debe llamarse in_range'


@pytest.mark.parametrize('value, lower_limit, upper_limit, expected', testdata)
@pytest.mark.dependency(depends=['test_func_exists'])
def test_run(value, lower_limit, upper_limit, expected):
    assert main.in_range(value, lower_limit, upper_limit) == expected
