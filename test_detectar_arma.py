from defer import return_value
from zmq import NULL
import socketio
import pytest
import numpy as np
from control import *
from unittest.mock import patch
import cv2



sio = socketio.Client()
gun_cascade = cv2.CascadeClassifier('cascade.xml')
frame = cv2.imread('./test/killbill.jpg')
@pytest.mark.parametrize(
    "input_a,input_b,input_c",
    [
        (None, np.empty_like(frame), np.empty_like(frame)),
        (sio, np.empty_like(frame), frame),
        (sio, gun_cascade, frame),
        (None, gun_cascade, frame),
        (sio, gun_cascade, np.empty_like(frame)),
    ]
)

def test_detectar_arma(input_a, input_b, input_c):
    input_c = imutils.resize(input_c, width=500)
    gray = cv2.cvtColor(input_c, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    gun = input_b.detectMultiScale(gray, 1.3, 5, minSize=(100, 100))
    patch('control.transmitirVideo', return_value=None)
    assert detectar_arma(input_a, gun, input_c) == None
