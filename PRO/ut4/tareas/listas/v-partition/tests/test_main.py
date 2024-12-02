import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([4, 3, 2, 9, 8, 5], 4, [[3, 2], [4, 9, 8, 5]]),
    ([5, 3, 8, 7, 11, 19, 12, 15], 10, [[5, 3, 8, 7], [11, 19, 12, 15]]),
    ([1, 2, 3], 10, [[1, 2, 3], []]),
    ([1, 2, 3], -10, [[], [1, 2, 3]]),
]


@pytest.mark.parametrize('values, ref_value, expected', testdata)
def test_run(values, ref_value, expected):
    assert main.run(values, ref_value) == expected
