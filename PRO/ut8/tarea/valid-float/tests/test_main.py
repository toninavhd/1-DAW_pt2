import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = (
    ('3', False),
    ('3.14', True),
    ('3.54_000_321', True),
    ('.5', True),
    ('-0.5', True),
    ('-.5', False),
    ('-5', False),
    ('-5.', True),
    ('3e2', True),
    ('3e2.5', False),
    ('-', False),
    ('+', False),
    ('11_345.879', True),
)


@pytest.mark.parametrize('number, expected', testdata)
def test_run(number, expected):
    assert main.run(number) == expected
