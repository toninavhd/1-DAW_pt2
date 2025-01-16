import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (
        {'math': 9.75, 'biology': 6.83, 'art': 5.42, 'english': 7.50},
        ('biology', 'art'),
        {'biology': 6.83, 'art': 5.42},
    ),
    (
        {'z': 2, 'y': 1, 'x': 0},
        ('x',),
        {'x': 0},
    ),
    (
        {'soup': 9, 'chicken': 14, 'rice': 7, 'burger': 10, 'steak': 15},
        ('rice', 'chicken', 'steak'),
        {'rice': 7, 'chicken': 14, 'steak': 15},
    ),
]


@pytest.mark.parametrize('data, target_keys, expected', testdata)
def test_run(data, target_keys, expected):
    assert main.run(data, target_keys) == expected
