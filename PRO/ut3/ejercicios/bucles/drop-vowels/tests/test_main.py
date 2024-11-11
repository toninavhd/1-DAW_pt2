import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('sergio delgado quintero', 'srg dlgd qntr'),
    ('PEPE BENAVENTE', 'PP BNVNT'),
    ('volando VOY, volando VENGO', 'vlnd VY, vlnd VNG'),
    ('Por favor, elimina mis vocales. ¡Gracias!', 'Pr fvr, lmn ms vcls. ¡Grcs!'),
]


@pytest.mark.parametrize('text, expected', testdata)
def test_run(text, expected):
    assert main.run(text) == expected
