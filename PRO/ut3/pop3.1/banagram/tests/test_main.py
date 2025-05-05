import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('gabana', 'banagrama', True),
    ('caprese', 'supermercado', True),
    ('Voluta', 'AUTOMOVIL', True),
    ('Burguesa', 'Hamburguesa', True),
    ('potaje', 'espejo', False),
    ('vano', 'Ventana', False),
    ('dispuesto', 'DISPOSITIVO', False),
    ('MONITOR', 'romina', False),
]


@pytest.mark.parametrize('word1, word2, expected', testdata)
def test_run(word1, word2, expected):
    assert main.run(word1, word2) == expected
