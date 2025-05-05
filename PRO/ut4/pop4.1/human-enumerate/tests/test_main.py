import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('apples', 'apples'),
    ('apples:oranges', 'apples and oranges'),
    ('apples:oranges:bananas', 'apples, oranges and bananas'),
    ('apples:oranges:bananas:lemons', 'apples, oranges, bananas and lemons'),
]


@pytest.mark.parametrize('items, expected', testdata)
def test_run(items, expected):
    assert main.run(items) == expected
