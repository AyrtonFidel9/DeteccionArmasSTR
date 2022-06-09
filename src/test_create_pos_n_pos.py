from defer import return_value
import pytest
import load_images_neg as load
from unittest.mock import patch
from defer import return_value

@pytest.mark.parametrize(
    "dire",
   [
        (""),
        ("/images/imagespositives")
    ]
)
#@patch("load.create_pos_n_pos", return_value=None)
def test_create_pos_n_pos(dire):
    path = dire
    assert load.create_pos_n_pos(path) == None

if __name__ == '__main__':
    pytest.main()
