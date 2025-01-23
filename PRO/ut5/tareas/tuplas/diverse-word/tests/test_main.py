import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (['blue', 'orange', 'green', 'yellow'], 'orange'),
    (['dictionary', 'turtle', 'flexibility', 'humanity'], 'dictionary'),
    (['light', 'environment', 'watermelon', 'happiness'], 'watermelon'),
    (
        ['telescope', 'blackboard', 'microprocessor', 'incomprehensibility', 'destination'],
        'incomprehensibility',
    ),
]


@pytest.mark.parametrize('words, expected', testdata)
def test_run(words, expected):
    assert main.run(words) == expected
