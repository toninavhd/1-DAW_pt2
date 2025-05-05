import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (0, ''),
    (10, 'abcdefghij'),
    (43, 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopq'),
    (
        99,
        'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstu',
    ),
]


@pytest.mark.dependency()
def test_func_exists():
    assert getattr(
        main, 'cycle_alphabet', None
    ), 'La función principal debe llamarse cycle_alphabet'


@pytest.mark.parametrize('num_chars, expected', testdata)
@pytest.mark.dependency(depends=['test_func_exists'])
def test_expected(num_chars, expected):
    assert ''.join(main.cycle_alphabet(num_chars)) == expected
