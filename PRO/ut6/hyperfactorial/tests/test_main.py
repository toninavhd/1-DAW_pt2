import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (1, 1),
    (3, 108),
    (5, 86400000),
    (7, 3319766398771200000),
]


@pytest.mark.dependency()
def test_func_exists():
    assert getattr(
        main, 'hyperfactorial', None
    ), 'La función principal debe llamarse hyperfactorial'


@pytest.mark.parametrize('n, expected', testdata)
@pytest.mark.dependency(depends=['test_func_exists'])
def test_expected(n, expected):
    assert main.hyperfactorial(n) == expected
