import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([], []),
    ([1], [1]),
    ([2, 1], [1, 2]),
    ([4, 9, 1, 5], [1, 4, 5, 9]),
    ([3, 3, 3, 2, 2, 1], [1, 2, 2, 3, 3, 3]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
]


@pytest.mark.dependency()
def test_func_exists():
    assert getattr(main, 'bsort', None), 'La función principal debe llamarse bsort'


@pytest.mark.parametrize('items, expected', testdata)
@pytest.mark.dependency(depends=['test_func_exists'])
def test_expected(items, expected):
    assert main.bsort(items) == expected
