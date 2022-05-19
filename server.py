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
    print("connect ", sid)

@sio.event
def msg(sid, data):
    print(sid, " message ", data)
    sio.emit('notification', {'msg':data})

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

@sio.event
def livestream(sid,video):
    # print(sid," frames: ",video)
    sio.emit('video', {'data': video})


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 8080)), app)