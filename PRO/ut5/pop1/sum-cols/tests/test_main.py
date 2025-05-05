import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('data/matrix1.dat', [42, 8, 30]),
    ('data/matrix2.dat', [11, -59, -22, -19, 11, 17, -72]),
    ('data/matrix3.dat', [299, 271, 434, 250]),
]


@pytest.mark.parametrize('input_path, expected', testdata)
def test_run(input_path, expected):
    assert main.run(input_path) == expected
