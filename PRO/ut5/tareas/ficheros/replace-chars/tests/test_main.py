import filecmp
import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (
        'data/noticia.input.txt',
        'aA|eE|iI|oO|uU',
        'data/noticia.output.1.txt',
        'data/noticia.expected.1.txt',
    ),
    (
        'data/noticia.input.txt',
        'áa|ée|íi|óo|úu',
        'data/noticia.output.2.txt',
        'data/noticia.expected.2.txt',
    ),
    (
        'data/noticia.input.txt',
        'ñn',
        'data/noticia.output.3.txt',
        'data/noticia.expected.3.txt',
    ),
]


@pytest.mark.parametrize('input_path, replacements, output_path, expected', testdata)
def test_run(input_path, replacements, output_path, expected):
    main.run(input_path, replacements, output_path)
    assert filecmp.cmp(output_path, expected, shallow=False)
