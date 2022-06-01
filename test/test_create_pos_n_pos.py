from zmq import NULL
import socketio
import pytest
from load_images_neg import *
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
    assert create_pos_n_pos(path) == None