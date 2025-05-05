import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = (
    ('info@iespuertodelacruz.es', True),
    ('info@', False),
    ('info@iespto.gobcan.edu.es', True),
    ('info@iespto', False),
    ('info-alumnado@iespto.gobcan.edu.es', True),
    ('info$alumnado@iespto.gobcan.edu.es', False),
    ('info@iespto.gobcan.edu.es/', False),
    ('info@iespto.gobcan.edu.es/blog/', False),
    ('info.edu.es', False),
    ('info$edu.es', False),
    ('info001@edu24.es', True),
    ('info.secretaria@iespuertodelacruz.es', True),
    ('info.secretaria.admision@iespuertodelacruz.es', True),
    ('$@$', False),
    ('$@$.com', False),
)


@pytest.mark.parametrize('email, expected', testdata)
def test_run(email, expected):
    assert main.run(email) == expected
