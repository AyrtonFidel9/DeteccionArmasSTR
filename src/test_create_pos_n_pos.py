import pytest
import load_images_neg as load
from unittest.mock import patch

@pytest.mark.parametrize(
    "dire",
    [
        (""),
        ("/images/imagespositives")
    ]
)
#@patch("load_image_neg.create_pos_n_pos")
def test_create_pos_n_pos(dire):
    path = dire
    assert load.create_pos_n_pos(path) == None