import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([1, 2, 3, 4, 5, 6, 7], 3, 4),
    (['Ana', 'Sara', 'Noelia'], 'Sara', 'Noelia'),
    ([3.21, 9.54, 6.32, 9.99], 6.32, 9.99),
    (['azul', 'amarillo', 'verde', 'amarillo', 'rojo'], 'amarillo', 'verde'),
    ([1, 2, 3], 4, None),
    ([1, 2, 3], 3, None),
]


@pytest.mark.parametrize('items, ref_item, expected', testdata)
def test_run(items, ref_item, expected):
    assert main.run(items, ref_item) == expected
