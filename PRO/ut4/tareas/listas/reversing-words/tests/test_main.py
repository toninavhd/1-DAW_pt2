import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('This is awesome', 'awesome is this'),
    ('Hello World', 'world hello'),
    ('Esto es Python', 'python es esto'),
    ('último caso de comprobación', 'comprobación de caso último'),
]


@pytest.mark.parametrize('text, expected', testdata)
def test_run(text, expected):
    assert main.run(text) == expected
