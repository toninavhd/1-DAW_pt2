import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('Kernighan,Brian', 5),
    ('RITCHIE,Dennis', 7),
    ('van Rossum,Guido', 5),
]


@pytest.mark.parametrize('fullname, expected', testdata)
def test_run(fullname, expected):
    assert main.run(fullname) == expected
