import pytest

from server import *


@pytest.mark.parametrize(
    ["sid", "environ", "salida"],
    [
        ('id', 'http://localhost:8080', None),
        (None, None, 'The connection failed!'),
        ('id', None, 'The connection failed!'),
        (None, 'http://localhost:8080', 'The connection failed!')
    ]
)
def test_connectparametro(sid, environ, salida):
    assert connect(sid, environ) == salida


@pytest.mark.parametrize(
    ["sid", "salida"],
    [
        ('id', None),
        (None, 'error')
    ]
)
def test_desconectado(sid, salida):
    assert disconnect(sid) == salida


@pytest.mark.parametrize(
    ["sid", "data", "salida"],
    [
        ('id', 'imagen', None),
        (None, None, 'Error'),
        ('id', None, 'Error'),
        (None, 'imagen', 'Error')
    ]
)
def test_msg(sid, data, salida):
    assert msg(sid, data) == salida