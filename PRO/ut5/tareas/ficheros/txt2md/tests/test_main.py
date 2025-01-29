import filecmp
import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('data/animals.input.txt', 'data/animals.output.md', 'data/animals.expected.md'),
    ('data/os.input.txt', 'data/os.output.md', 'data/os.expected.md'),
    ('data/db.input.txt', 'data/db.output.md', 'data/db.expected.md'),
]


@pytest.mark.parametrize('input_path, output_path, expected', testdata)
def test_run(input_path, output_path, expected):
    main.run(input_path, output_path)
    assert filecmp.cmp(output_path, expected, shallow=False)
