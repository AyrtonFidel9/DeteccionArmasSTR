import socketio
import eventlet
import eventlet.wsgi
from flask import Flask, render_template, request

sio = socketio.Server()
app = Flask(__name__)
app.wsgi_app = socketio.WSGIApp(sio, static_files={
    '/': "./public/"
})


@app.route('/')
def index():
    return render_template('index.html')


@sio.event
def connect(sid, environ):
    try:
        if sid is None or environ is None:
            raise Exception("The connection failed!")
        else:
            print("connect ", sid)
    except Exception as e:
        return str(e)


@sio.event
def msg(sid, data):
    try:
        if sid is None or data is None:
            raise  Exception('Error')
        else:
            print(sid, " message ", data)
            sio.emit('notification', {'msg': data})
    except Exception as e:
        return str(e)

@sio.event
def disconnect(sid):
    try:
        if sid is None:
            raise Exception('error')
        else:
            print('disconnect ', sid)
    except Exception as e:
        return str(e)


@sio.event
def livestream(sid, video):
    # print(sid," frames: ",video)
    sio.emit('video', {'data': video})


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 8080)), app)
