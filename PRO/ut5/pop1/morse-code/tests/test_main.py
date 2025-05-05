import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('data/signals.morse', 'hello, world!', '.... . .-.. .-.. --- .-- --- .-. .-.. -..'),
    (
        'data/signals.morse',
        'now is better than never!',
        '-. --- .-- .. ... -... . - - . .-. - .... .- -. -. . ...- . .-.',
    ),
    ('data/signals.morse', 'Believe in YOU 😀', '-... . .-.. .. . ...- . .. -. -.-- --- ..-'),
    ('data/signals.morse', 'Count to 10!', '-.-. --- ..- -. - - --- .---- -----'),
]


@pytest.mark.parametrize('morse_path, sentence, expected', testdata)
def test_run(morse_path, sentence, expected):
    assert main.run(morse_path, sentence) == expected
