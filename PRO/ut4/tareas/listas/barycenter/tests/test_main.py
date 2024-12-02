import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([4, 6], [12, 4], [10, 10], (8.6667, 6.6667)),
    ([4, 2], [12, 2], [6, 10], (7.3333, 4.6667)),
]


@pytest.mark.parametrize('A, B, C, expected', testdata)
def test_run(A, B, C, expected):
    assert main.run(A, B, C) == expected
