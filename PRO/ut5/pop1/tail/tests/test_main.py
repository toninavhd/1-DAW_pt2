import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('data/zen.txt', 1, "Namespaces are one honking great idea -- let's do more of those!"),
    (
        'data/zen.txt',
        3,
        "If the implementation is hard to explain, it's a bad idea.\nIf the implementation is easy to explain, it may be a good idea.\nNamespaces are one honking great idea -- let's do more of those!",
    ),
    (
        'data/zen.txt',
        5,
        "Now is better than never.\nAlthough never is often better than *right* now.\nIf the implementation is hard to explain, it's a bad idea.\nIf the implementation is easy to explain, it may be a good idea.\nNamespaces are one honking great idea -- let's do more of those!",
    ),
    (
        'data/zen.txt',
        10,
        "Errors should never pass silently.\nUnless explicitly silenced.\nIn the face of ambiguity, refuse the temptation to guess.\nThere should be one-- and preferably only one --obvious way to do it.\nAlthough that way may not be obvious at first unless you're Dutch.\nNow is better than never.\nAlthough never is often better than *right* now.\nIf the implementation is hard to explain, it's a bad idea.\nIf the implementation is easy to explain, it may be a good idea.\nNamespaces are one honking great idea -- let's do more of those!",
    ),
]


@pytest.mark.parametrize('input_path, n, expected', testdata)
def test_run(input_path, n, expected):
    assert main.run(input_path, n) == expected
