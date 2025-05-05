import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (lambda: 3.14159, [], {}, 0, 3),
    (lambda: 3.14159, [], {}, 1, 3.1),
    (lambda: 3.14159, [], {}, 2, 3.14),
    (lambda: 3.14159, [], {}, 3, 3.142),
    (lambda: 3.14159, [], {}, 4, 3.1416),
    (lambda: 3.14159, [], {}, 5, 3.14159),
]


@pytest.mark.dependency()
def test_decorator_exists():
    assert getattr(main, 'cround'), 'El decorador debe llamarse cround'


@pytest.mark.dependency(depends=['test_decorator_exists'])
@pytest.mark.parametrize('func, func_args, func_kwargs, ndecimals, expected', testdata)
def test_result(func, func_args, func_kwargs, ndecimals, expected):
    assert main.run(func, ndecimals, func_args, func_kwargs) == expected
