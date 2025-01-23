import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('And all the roads', 'We have to walk are winding', 'dhlnrt'),
    ('Flat is bEtter than nested', 'Readability counts', 'bdlnrst'),
    ('Now is better thAn never', 'Beautiful is better than ugly', 'bhnrst'),
    ('Hello', 'Bye', ''),
]


@pytest.mark.parametrize('text1, text2, expected', testdata)
def test_run(text1, text2, expected):
    assert main.run(text1, text2) == expected
