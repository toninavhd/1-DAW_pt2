import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([7, 3, 1, 12, 21, 4], 8, 13),
    ([-5, -9, 12, 18], 15, 24),
    ([1, 1, 1], 1, 0),
    ([], 1, 0),
]


@pytest.mark.parametrize('values, target, expected', testdata)
def test_run(values, target, expected):
    assert main.run(values, target) == expected
