import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (20, [5, 2, 1], {5: 4}),
    (7, [2, 1, 0.5], {2: 3, 1: 1}),
    (13.50, [5, 2, 0.5], {5: 2, 2: 1, 0.5: 3}),
    (11, [0.10, 0.5, 2], {2: 5, 0.5: 2.0}),
    (0, [0.5, 0.20, 0.10], {}),
    (4.75, [1, 5, 0.20], None),
]


@pytest.mark.parametrize('to_give_back, available_currencies, expected', testdata)
def test_run(to_give_back, available_currencies, expected):
    assert main.run(to_give_back, available_currencies) == expected
