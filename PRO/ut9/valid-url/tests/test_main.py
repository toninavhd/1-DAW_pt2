import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = (
    ('http://iespuertodelacruz.es', True),
    ('https://iespuertodelacruz.es', True),
    ('http://iespuertodelacruz', False),
    ('https://iespuertodelacruz', False),
    ('http://iespuertodelacruz.gobcan.edu.org', True),
    ('https://iespuertodelacruz.gobcan.edu.org', True),
    ('https://iespuerto-de-la-cruz.es', True),
    ('https://-.-.-.-', False),
    ('https://iespuertodelacruz.gobcan.edu.org/blog', True),
    ('https://iespuertodelacruz.gobcan.edu.org/blog/', True),
    ('https://iespuertodelacruz.gobcan.edu.org/blog/hero', True),
    ('https://iespuertodelacruz.gobcan.edu.org/blog/hero/launch', True),
    ('https://iespuertodelacruz.gobcan.edu.org/blog/index.html', True),
    ('https://iespuertodelacruz.gobcan.edu.org/blog/index.html/', False),
    ('https://iespuertodelacruz/blog/index.html', False),
    ('https://iespuerto-001.com', True),
    ('https://iespuerto-001.com/news/21/', True),
    ('https://$$$.!!!', False),
)


@pytest.mark.parametrize('url, expected', testdata)
def test_run(url, expected):
    assert main.run(url) == expected
