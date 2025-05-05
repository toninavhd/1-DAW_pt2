import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('(161,49,247)', (161, 49, 247)),
    ('(255,17,255)', (255, 17, 255)),
    ('(18,52,86)', (18, 52, 86)),
]


@pytest.mark.parametrize('rgb_color, expected', testdata)
def test_run(rgb_color, expected):
    assert main.run(rgb_color) == expected
