import pytest
from requests import patch
from unittest.mock import patch
import socketio

from control import *


@patch("control.iniciar_Reconocimiento")
def test_iniciar_Reconocimiento(patched):
    return_value = "I'm connected!"
    sio = socketio.Client()
    gun_cascade = cv2.CascadeClassifier('../cascade.xml')
    camera = cv2.VideoCapture(0)
    msg = iniciar_Reconocimiento(sio, gun_cascade, camera)
    assert msg == "I'm connected!"


@patch("control.decodificarVideo",
       return_value="frame")
def test_decodificarvideo(patched):
    frame = [[1, 2, 3], [4, 5, 6]]
    msg = decodificarVideo(frame)
    assert msg == "frame"
