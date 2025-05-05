import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('c2f', 32.19, 89.94),
    ('c2f', 29.75, 85.55),
    ('f2c', 93.21, 34.01),
    ('f2c', 64.39, 17.99),
    ('a2b', 10.21, None),
]


@pytest.mark.parametrize('schema, temp, expected', testdata)
def test_run(schema, temp, expected):
    result = main.run(schema, temp)
    if expected is None:
        assert result is None
    else:
        assert round(result, 2) == expected
