import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (
        ['AZUL', 'blanco', 'NEGRO', 'amarillo'],
        (['blanco', 'amarillo'], ['AZUL', 'NEGRO']),
    ),
    (
        ['FEDORA', 'debian', 'OPENSUSE', 'ubuntu', 'MacOS'],
        (['debian', 'ubuntu'], ['FEDORA', 'OPENSUSE']),
    ),
    (
        ['python', 'c', 'javascript'],
        (['python', 'c', 'javascript'], []),
    ),
]


@pytest.mark.dependency()
def test_func_exists():
    assert getattr(main, 'split_case', None), 'La función principal debe llamarse split_case'


@pytest.mark.parametrize('words, expected', testdata)
@pytest.mark.dependency(depends=['test_func_exists'])
def test_expected(words, expected):
    assert main.split_case(words) == expected
