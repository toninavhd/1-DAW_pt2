import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('[3,10]', [3, 4, 5, 6, 7, 8, 9, 10]),
    ('(3,10]', [4, 5, 6, 7, 8, 9, 10]),
    ('[3,10)', [3, 4, 5, 6, 7, 8, 9]),
    ('(3,10)', [4, 5, 6, 7, 8, 9]),
    ('[20,24)', [20, 21, 22, 23]),
    ('[101,103]', [101, 102, 103]),
    ('(2001,2006)', [2002, 2003, 2004, 2005]),
]


@pytest.mark.parametrize('interval, expected', testdata)
def test_run(interval, expected):
    assert main.run(interval) == expected
