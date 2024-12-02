import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([1, 3, 7], True),
    ([7, 1, 2, 3], False),
    ([1, 3, 5, 7], False),
    ([1, 5, 6, 7, 3], True),
    ([5, 6, 7], True),
    ([5, 6, 7, 8], True),
    ([6, 7, 8], False),
    ([7, 8], True),
]


@pytest.mark.parametrize('formula, expected', testdata)
def test_run(formula, expected):
    assert main.run(formula) == expected
