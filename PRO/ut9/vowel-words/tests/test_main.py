import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = (
    ('hola ana cómo estás', ['ana', 'estás']),
    ('hola!ana cómo estás', ['ana', 'estás']),
    ('hola! ana cómo estás', ['ana', 'estás']),
    ('hola ana ¿cómo?estás', ['ana', 'estás']),
    ('hola ana ¿cómo?estás?', ['ana', 'estás']),
    ('hola ANA ¿cómo Estás?', ['ANA', 'Estás']),
    ('hola;Ana;cómo;Estás;', ['Ana', 'Estás']),
    ('hola ana cómo estás, ¿a dónde vas?', ['ana', 'estás', 'a']),
    ('hola ana cómo estás ¿a_ dónde vas?', ['ana', 'estás', 'a']),
    ('Vamos Ana ¡eres la última!', ['Ana', 'eres', 'última']),
)


@pytest.mark.parametrize('x, expected', testdata)
def test_run(x, expected):
    assert main.run(x) == expected
