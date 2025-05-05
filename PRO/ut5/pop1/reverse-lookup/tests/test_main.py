import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ({'A': 1, 'B': 2, 'C': 3, 'D': 3, 'E': 4}, 3, ['C', 'D']),
    ({'Z': 10, 'Y': 10, 'X': 10}, 10, ['X', 'Y', 'Z']),
    ({'U': 5, 'V': 6, 'W': 7, 'R': 8}, 4, []),
    ({'U': 5, 'V': 6, 'W': 7, 'R': 8}, 8, ['R']),
]


@pytest.mark.parametrize('data, target_value, expected', testdata)
def test_run(data, target_value, expected):
    assert main.run(data, target_value) == expected
