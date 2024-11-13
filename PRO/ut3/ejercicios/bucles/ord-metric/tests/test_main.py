import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('probando', 106.62),
    ('Buena suerte', 98.92),
    ('Yo escribo Python', 97.00),
    ('paz', 110.33),
]


@pytest.mark.parametrize('text, expected', testdata)
def test_run(text, expected):
    assert main.run(text) == expected
