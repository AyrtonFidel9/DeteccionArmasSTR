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
    camera = cv2.VideoCapture(0)
    gun_cascade = cv2.CascadeClassifier('./cascade.xml')

    (grabbed, frame) = camera.read()

    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    gun = gun_cascade.detectMultiScale(gray, 1.3, 5, minSize=(100, 100))

    for (x, y, w, h) in gun:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        print("frame: ", frame)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
    # draw the text and timestamp on the frame
    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

    msg = decodificarVideo(frame)
    assert msg == "frame"
