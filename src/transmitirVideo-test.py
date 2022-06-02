import unittest
import socketio
from socket import socket

from unittest.mock import patch, create_autospec


class transmitirVideo(unittest.TestCase):

    @patch("socket.ioclient")
    def test_comprobarTransmision(self,mock_patch):
        def decodificarVideo(frame):
            pass

        sio = socketio.Server()
        mock_decodificarVideo = create_autospec(decodificarVideo, return_value='[1,2,3]')

        assert(mock_decodificarVideo)




if __name__ == '__main__':
    unittest.main()
