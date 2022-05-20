import pytest
from server import *

def test_connectparametro():
    sid="id"
    environ = "http://localhost:8080"
    assert connect(sid, environ) == None

def test_desconectado():
    sid = "id"
    assert disconnect(sid) == None

def test_msg():
    sid="id"
    data="imagen"
    assert msg(sid,data)==None