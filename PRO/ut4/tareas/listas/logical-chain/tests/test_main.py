import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([True, True, False], 'and', False),
    ([True, True, False], 'or', True),
    ([True, True, True], 'and', True),
    ([False, False, False], 'and', False),
]


@pytest.mark.parametrize('values, oper, expected', testdata)
def test_run(values, oper, expected):
    assert main.run(values, oper) == expected
