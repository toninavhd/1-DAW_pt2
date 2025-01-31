import filecmp
import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (
        'data/matrix1A.input.dat',
        'data/matrix1B.input.dat',
        'data/matrix1.output.dat',
        'data/matrix1.expected.dat',
    ),
    (
        'data/matrix2A.input.dat',
        'data/matrix2B.input.dat',
        'data/matrix2.output.dat',
        'data/matrix2.expected.dat',
    ),
    (
        'data/matrix3A.input.dat',
        'data/matrix3B.input.dat',
        'data/matrix3.output.dat',
        'data/matrix3.expected.dat',
    ),
]


@pytest.mark.parametrize('matrix1_path, matrix2_path, result_path, expected', testdata)
def test_run(matrix1_path, matrix2_path, result_path, expected):
    main.run(matrix1_path, matrix2_path, result_path)
    assert filecmp.cmp(result_path, expected, shallow=False)
