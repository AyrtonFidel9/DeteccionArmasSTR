from defer import return_value
import pytest
from load_images_neg import find_uglies
from unittest.mock import patch

@pytest.mark.parametrize(
    ["dir", "result"],
    [
        ('/images/negativeimages', "[Errno 2] No such file or directory: '/images/negativeimages/neg'"),
        (None, "Path not found")
    ]
)
#@patch("find_uglies", return_value=None)
def test_find_uglies(dir, result):
    assert find_uglies(dir) == result
