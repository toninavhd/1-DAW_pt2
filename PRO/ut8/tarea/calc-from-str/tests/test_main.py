import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = (
    ('3+2', 5),
    ('3-2', 1),
    ('3*2', 6),
    ('3/2', 1.5),
    ('3 / 2', 1.5),
    ('30 -24', 6),
)


@pytest.mark.parametrize('expression, expected', testdata)
def test_run(expression: str, expected: list[str]):
    assert main.run(expression) == expected


@pytest.mark.skip()
def test_calc_fails_when_operator_is_not_supported():
    with pytest.raises(ValueError) as err:
        main.run('3@2')
    assert str(err.value) == 'Operator @ is not supported!'
