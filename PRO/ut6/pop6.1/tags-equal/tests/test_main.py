import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('<img src="cat.jpg" width=30>', '<IMG src="dog.jpg">', True),
    ('<div class="contents">', '<div>', True),
    ('<p style="color: red">', '<table style="color: green">', False),
    ('<head id="main">', '<div id="main">', False),
]


@pytest.mark.parametrize('tag1, tag2, expected', testdata)
def test_run(tag1, tag2, expected):
    assert main.run(tag1, tag2) == expected
