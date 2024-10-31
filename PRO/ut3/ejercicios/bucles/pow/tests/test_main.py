import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (3, 4, 81),
    (5, 9, 1_953_125),
    (7, 14, 678_223_072_849),
]


@pytest.mark.parametrize('x, n, expected', testdata)
def test_run(x, n, expected):
    assert main.run(x, n) == expected
