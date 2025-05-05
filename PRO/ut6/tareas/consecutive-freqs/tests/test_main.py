import inspect
import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5], False, [(1, 1), (2, 3), (4, 3), (5, 4)]),
    ([1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5], True, '1:1,2:3,4:3,5:4'),
    ([], False, []),
    ([], True, ''),
    ([1], False, [(1, 1)]),
    ([1], True, '1:1'),
    ([0, 1], False, [(0, 1), (1, 1)]),
    ([0, 1], True, '0:1,1:1'),
    ([0, 0, 9, 5, 5, 5, 1, 1, 1], False, [(0, 2), (9, 1), (5, 3), (1, 3)]),
    ([1, 2, 3], True, '1:1,2:1,3:1'),
    ([2, 2, 1, 1, 2, 2, 1, 1], False, [(2, 2), (1, 2), (2, 2), (1, 2)]),
    ([2, 2, 1, 1, 2, 2, 1, 1], True, '2:2,1:2,2:2,1:2'),
]


@pytest.mark.dependency()
def test_func_exists():
    assert getattr(main, 'cfreq', None), 'La función principal debe llamarse cfreq'


@pytest.mark.parametrize('items, as_string, expected', testdata)
@pytest.mark.dependency(depends=['test_func_exists'])
def test_expected(items, as_string, expected):
    assert main.cfreq(items, as_string) == expected


@pytest.mark.dependency(depends=['test_func_exists'])
def test_params():
    param1, param2 = inspect.signature(main.cfreq).parameters.values()
    assert param1.kind == param1.POSITIONAL_ONLY, 'El primer parámetro debe ser sólo posicional'
    assert param2.default is False, 'El segundo parámetro debe tener valor por defecto a falso'
