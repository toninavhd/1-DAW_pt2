import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([1, [2, 4], 5, [6, [7, 8]]], 33),
    ([10, [5, 6, [7, [8, 9]]]], 45),
    ([1, [2, [3, [4]]]], 10),
    ([], 0),
]


@pytest.mark.dependency()
def test_func_exists():
    assert getattr(main, 'add', None), 'La función principal debe llamarse add'


@pytest.mark.parametrize('items, expected', testdata)
@pytest.mark.dependency(depends=['test_func_exists'])
def test_expected(items, expected):
    assert main.add(items) == expected
