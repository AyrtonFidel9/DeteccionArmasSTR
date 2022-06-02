import pytest
from src import load_images_neg as load
from unittest.mock import patch

@pytest.mark.parametrize(
    "dire",
    [
        (""),
        ("/mnt/d/Development/positivesimages")
    ]
)
#@patch("load_image_neg.create_pos_n_pos")
def test_create_pos_n_pos(dire):
    path = dire
    assert load.create_pos_n_pos(path) == None