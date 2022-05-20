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

