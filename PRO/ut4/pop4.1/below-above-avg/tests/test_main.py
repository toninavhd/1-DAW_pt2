import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (
        [3.7, 1.2, 9.5, 4.7, 6.3, 7.2, 3.8, 1.1, 1.4],
        ([3.7, 1.2, 3.8, 1.1, 1.4], [9.5, 4.7, 6.3, 7.2]),
    ),
    (
        [0, 3.8, 1.2, 1.9, 4.7, 5.1, 3.6, 4.4, 9.2, 7.4],
        ([0, 3.8, 1.2, 1.9, 3.6], [4.7, 5.1, 4.4, 9.2, 7.4]),
    ),
    (
        [9.9, 9.7, 5.6, 1.8, 4.3, 7.5, 6.6, 6.4],
        ([5.6, 1.8, 4.3, 6.4], [9.9, 9.7, 7.5, 6.6]),
    ),
]


@pytest.mark.parametrize('marks, expected', testdata)
def test_run(marks, expected):
    assert main.run(marks) == expected
