import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (
        'data/help.txt',
        'you',
        [
            (3, 8),
            (10, 12),
            (11, 21),
            (13, 7),
            (18, 41),
            (20, 12),
            (21, 21),
            (23, 7),
            (30, 12),
            (31, 21),
            (33, 7),
        ],
    ),
    ('data/help.txt', 'round', [(11, 32), (21, 32), (31, 32)]),
    ('data/help.txt', 'days', [(6, 21), (6, 42), (26, 21), (26, 42)]),
    ('data/help.txt', 'then', [(16, 25), (16, 39)]),
]


@pytest.mark.parametrize('data_path, target_word, expected', testdata)
def test_run(data_path, target_word, expected):
    assert main.run(data_path, target_word) == expected
