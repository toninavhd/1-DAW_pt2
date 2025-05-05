import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('aaaantequera', 4),
    ('aeropuerto', 2),
    ('IiInteligencia', 3),
    ('Oouuuhhh', 5),
    ('Barcelona', 0),
]


@pytest.mark.parametrize('text, expected', testdata)
def test_run(text, expected):
    assert main.run(text) == expected
