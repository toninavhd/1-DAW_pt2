import filecmp
import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('data/temps1.input.dat', 'data/temps1.output.dat', 'data/temps1.expected.dat'),
    ('data/temps2.input.dat', 'data/temps2.output.dat', 'data/temps2.expected.dat'),
    ('data/temps3.input.dat', 'data/temps3.output.dat', 'data/temps3.expected.dat'),
]


@pytest.mark.parametrize('input_path, output_path, expected', testdata)
def test_run(input_path, output_path, expected):
    main.run(input_path, output_path)
    assert filecmp.cmp(output_path, expected, shallow=False)
