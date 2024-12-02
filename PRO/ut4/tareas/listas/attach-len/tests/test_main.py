import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('todo se transforma', ['todo:4', 'se:2', 'transforma:10']),
    ('test', ['test:4']),
    ('tiene mucha importancia', ['tiene:5', 'mucha:5', 'importancia:11']),
    ('flat is better than nested', ['flat:4', 'is:2', 'better:6', 'than:4', 'nested:6']),
]


@pytest.mark.parametrize('text, expected', testdata)
def test_run(text, expected):
    assert main.run(text) == expected
