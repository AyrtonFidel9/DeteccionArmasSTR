import pytest
import socketio
import cv2

from src.control import *

@pytest.mark.parametrize(
    ["sio", "gun_cascade", "camera", "salida"],
    [
        (socketio.Client(), cv2.CascadeClassifier("../cascade.xml"), cv2.VideoCapture(), None),
        (None, cv2.CascadeClassifier("../cascade.xml"), cv2.VideoCapture(), None),
        (socketio.Client(), None, cv2.VideoCapture(), None),
        (socketio.Client(), cv2.CascadeClassifier("../cascade.xml"), None, "Camera not found")
    ]
)
def test_iniciar_Reconocimiento(sio, gun_cascade, camera, salida):
    assert iniciar_Reconocimiento(sio, gun_cascade, camera) == salida


