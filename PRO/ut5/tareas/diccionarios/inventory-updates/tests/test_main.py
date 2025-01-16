import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('A1,B4,A-2,A7,B1,C4', {'A': 6, 'B': 5, 'C': 4}),
    ('X2,Y9,Z3,Y-2,Z-4,Y3,X-8,W5', {'X': -6, 'Y': 10, 'Z': -1, 'W': 5}),
    ('R-2,S0,S2,S-8,R21,R-3,S11,R4', {'R': 20, 'S': 5}),
]


@pytest.mark.parametrize('imoves, expected', testdata)
def test_run(imoves, expected):
    assert main.run(imoves) == expected
