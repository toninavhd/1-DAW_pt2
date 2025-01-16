import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ({'a': 'two', 'b': 'one', 'c': 'three'}, [('b', 'one'), ('c', 'three'), ('a', 'two')]),
    (
        {'mar': 'azul', 'tierra': 'marrón', 'aire': 'blanco'},
        [('mar', 'azul'), ('aire', 'blanco'), ('tierra', 'marrón')],
    ),
    (
        {'M': 'MacOS', 'L': 'Linux', 'W': 'Windows'},
        [('L', 'Linux'), ('M', 'MacOS'), ('W', 'Windows')],
    ),
    (
        {'C1': 'Red', 'C2': 'Black', 'C3': 'Red', 'C4': 'Green'},
        [('C2', 'Black'), ('C4', 'Green'), ('C1', 'Red'), ('C3', 'Red')],
    ),
    ({}, []),
]


@pytest.mark.parametrize('unsorted_items, expected', testdata)
def test_run(unsorted_items, expected):
    assert main.run(unsorted_items) == expected
