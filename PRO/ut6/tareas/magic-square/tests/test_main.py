import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([], True),
    ([[4, 9, 2], [3, 5, 7], [8, 1, 6]], True),
    ([[4, 9, 1], [3, 5, 7], [8, 1, 6]], False),
    ([[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 1]], True),
    ([[16, 3, 2, 12], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 1]], False),
    ([[1, 14, 14, 4], [11, 7, 6, 9], [8, 10, 10, 5], [13, 2, 3, 15]], True),
    ([[1, 14, 14, 3], [11, 7, 6, 9], [8, 10, 10, 5], [13, 2, 3, 15]], False),
    (
        [
            [49, 48, 11, 46, 6, 12, 3],
            [7, 13, 14, 31, 32, 35, 43],
            [8, 30, 28, 21, 26, 20, 42],
            [45, 33, 23, 25, 27, 17, 5],
            [9, 34, 24, 29, 22, 16, 41],
            [10, 15, 36, 19, 18, 37, 40],
            [47, 2, 39, 4, 44, 38, 1],
        ],
        True,
    ),
]


@pytest.mark.dependency()
def test_func_exists():
    assert getattr(
        main, 'is_magic_square', None
    ), 'La función principal debe llamarse is_magic_square'


@pytest.mark.parametrize('values, expected', testdata)
@pytest.mark.dependency(depends=['test_func_exists'])
def test_expected(values, expected):
    assert main.is_magic_square(values) == expected
