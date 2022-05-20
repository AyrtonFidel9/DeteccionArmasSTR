import pytest
from unittest.mock import patch

from load_images_neg import find_uglies

def test_find_uglies():
    with patch("load_images_neg.find_uglies",
               return_value = 'That is one ugly pic! Deleting!') as patched:
        dir = r'/Users/edwinmanzano/Documents/Dev/Opencv/opencv-haar-classifier-training/negative_images'
        msg = find_uglies(dir)
        assert msg == 'That is one ugly pic! Deleting!'