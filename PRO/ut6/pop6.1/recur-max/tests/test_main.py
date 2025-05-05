import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([5, 3, 9, 2, 7], 9),
    (['x', 'y', 'z'], 'z'),
    ([21, 34, 15, 11, 45, 32], 45),
    ([(1, 2), (6, 0), (4, 3)], (6, 0)),
    ([-4, -9, -1, -12, -3], -1),
]


@pytest.mark.parametrize('items, expected', testdata)
def test_run(items, expected):
    assert main.get_max(items) == expected
