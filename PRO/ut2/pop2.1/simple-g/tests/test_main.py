import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (5, 7, 0.0338062),
    (6, 2, 0.0481125),
    (21, 4, 0.0051957),
]


@pytest.mark.parametrize('a, b, expected', testdata)
def test_run(a, b, expected):
    assert main.run(a, b) == expected
