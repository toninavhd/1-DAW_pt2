import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([7, 3, 4, 8, 12, 6, 9], [7, 3, 9]),
    ([1, 2, 3, 4, 5], [1, 3, 5]),
    ([1, 1, 2, 2, 3, 3], [1, 3]),
    ([2, 4, 6], []),
]


@pytest.mark.parametrize('values, expected', testdata)
def test_run(values, expected):
    assert main.run(values) == expected
