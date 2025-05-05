import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([1, 74, 56, 56, 56, 332, 8, 8, 8], 3, 56),
    ([1, 10, 20, 30, 30, 30, 30, 30, 40, 50], 5, 30),
    ([11, 9, 20, 71, 51, 51, 2, 4, 4, 4, 4], 4, 4),
    ([7], 1, 7),
    ([77, 16, 99, 21, 1], 2, None),
]


@pytest.mark.dependency()
def test_func_exists():
    assert getattr(
        main, 'consecutive_seq', None
    ), 'La función principal debe llamarse consecutive_seq'


@pytest.mark.parametrize('items, num_reps, expected', testdata)
@pytest.mark.dependency(depends=['test_func_exists'])
def test_expected(items, num_reps, expected):
    assert main.consecutive_seq(items, num_reps) == expected
