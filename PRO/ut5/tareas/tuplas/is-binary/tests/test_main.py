import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('101011010111', True),
    ('101101013101', False),
    ('1', True),
    ('0', True),
    ('A', False),
    ('125', False),
    ('111111', True),
    ('000000', True),
]


@pytest.mark.parametrize('number, expected', testdata)
def test_run(number, expected):
    assert main.run(number) == expected
