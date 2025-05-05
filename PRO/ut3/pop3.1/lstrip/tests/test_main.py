import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('televisión', 'tle', 'visión'),
    ('955428P4YLO4D001', '0123456789', 'P4YLO4D001'),
    ('aaaioueeooPaYLoaDi', 'aeiou', 'PaYLoaDi'),
    (';::-;..PAY-LOAD.', ',.:;-', 'PAY-LOAD.'),
]


@pytest.mark.parametrize('text, strip_chars, expected', testdata)
def test_run(text, strip_chars, expected):
    assert main.run(text, strip_chars) == expected
