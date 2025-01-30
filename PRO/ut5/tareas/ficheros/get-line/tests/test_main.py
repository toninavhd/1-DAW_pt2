import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (
        'data/mercurio.txt',
        1,
        'Mercurio es el planeta del sistema solar más cercano al Sol y el más pequeño.',
    ),
    (
        'data/mercurio.txt',
        3,
        'y carece de satélites naturales al igual que Venus.',
    ),
    (
        'data/mercurio.txt',
        0,
        None,
    ),
    (
        'data/saturno.txt',
        6,
        'El aspecto más característico de Saturno son sus brillantes y grandes anillos.',
    ),
    (
        'data/saturno.txt',
        4,
        'Su nombre proviene del dios romano Saturno.',
    ),
    (
        'data/saturno.txt',
        17,
        None,
    ),
]


@pytest.mark.parametrize('input_path, line_no, expected', testdata)
def test_run(input_path, line_no, expected):
    assert main.run(input_path, line_no) == expected
