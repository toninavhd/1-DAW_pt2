import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ({'pen': 20, 'cup': 11, 'keyring': 40}, 'cup', 9, True),
    ({'pen': 20, 'cup': 11, 'keyring': 40}, 'pen', 21, False),
    ({'pen': 20, 'cup': 11, 'keyring': 40}, 'keyring', 40, True),
    ({'pen': 20, 'cup': 11, 'keyring': 40}, 'popcorn', 5, False),
]


@pytest.mark.parametrize('stock, merch, amount, expected', testdata)
def test_run(stock, merch, amount, expected):
    assert main.run(stock, merch, amount) == expected
