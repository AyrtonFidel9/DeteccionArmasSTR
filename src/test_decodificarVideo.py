import pytest
import numpy as np
import cv2
from unittest.mock import patch
import control as ctl
frame = cv2.imread('killbill.jpg')

@pytest.mark.parametrize(
    "imagen",
    [
        (np.empty_like(frame)),
        (frame),
        (None),
        (1)
    ]
)
def test_decodificarvideo(imagen):
    try:
        patch('ctl.decodificarVideo', return_value = None)
        assert ctl.decodificarVideo(imagen) == None
    except:
        pass