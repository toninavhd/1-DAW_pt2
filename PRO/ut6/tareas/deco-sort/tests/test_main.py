import os
import random

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

input_values = list(range(10))
random.shuffle(input_values)

testdata = [
    (input_values, True, [0, 2, 4, 6, 8]),
    (input_values, False, [8, 6, 4, 2, 0]),
    (input_values, None, [0, 2, 4, 6, 8]),
]


@pytest.mark.dependency()
def test_decorator_exists():
    assert getattr(main, 'sort', None), 'El decorador debe llamarse sort'


@pytest.mark.parametrize('values, asc, expected', testdata)
def test_expected(values, asc, expected):
    deco_sort = main.sort() if asc is None else main.sort(asc)
    deco_func = deco_sort((lambda values: [v for v in values if v % 2 == 0]))
    assert deco_func(values) == expected
