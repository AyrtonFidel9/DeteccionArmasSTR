import pytest
from unittest.mock import patch

from DeteccionArmasSTR import control
from DeteccionArmasSTR.control import decodificarVideo

@patch("control.decodificarVideo", return_value="[0,1,2]")
def test_decodificarvideo(patched):
    frame = " "
    assert decodificarVideo(frame) == "[0,1,2]"