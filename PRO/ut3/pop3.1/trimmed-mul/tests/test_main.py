import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (3.21, 7.44, 0, 20.51, 20.51),
    (4.32, 1.71, 8.02, 19.46, 8.02),
    (2.86, 5.09, 1.03, 15.43, 14.56),
]


@pytest.mark.parametrize('value1, value2, vmin, vmax, expected', testdata)
def test_run(value1, value2, vmin, vmax, expected):
    assert main.run(value1, value2, vmin, vmax) == expected
