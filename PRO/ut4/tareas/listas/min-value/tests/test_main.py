import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([-11, 10, -6, 15, -1], -11),
    ([5, 9, -6, 9, -2, -9, -7, 2], -9),
    ([-7, -5, -5, -8, -3], -8),
]


@pytest.mark.parametrize('values, expected', testdata)
def test_run(values, expected):
    assert main.run(values) == expected
