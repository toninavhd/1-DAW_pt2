import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('data/python.txt', 'multiplataforma'),
    ('data/java.txt', 'implementaciones'),
]


@pytest.mark.parametrize('input_path, expected', testdata)
def test_run(input_path, expected):
    assert main.run(input_path) == expected
