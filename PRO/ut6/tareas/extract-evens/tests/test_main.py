import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 4, 6, 8]),
    ([8, 6, 1, 2, 3, 4], [8, 6, 2, 4]),
    ([], []),
    ([1, 3, 5], []),
    ([2, 2, 2], [2, 2, 2]),
]


@pytest.mark.dependency()
def test_func_exists():
    assert getattr(main, 'extract_evens', None), 'La función principal debe llamarse extract_evens'


@pytest.mark.parametrize('values, expected', testdata)
@pytest.mark.dependency(depends=['test_func_exists'])
def test_expected(values, expected):
    assert main.extract_evens(values) == expected
