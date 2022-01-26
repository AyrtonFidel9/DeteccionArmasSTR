import asyncio
import socketio
import video_recognition as vg
# asyncio
sio = socketio.AsyncClient()

@sio.event
async def connect():
    print("I'm connected!")

@sio.event
async def connect_error(data):
    print("The connection failed!")

@sio.event
async def my_message(data):
    print('message received with ', data)
    await sio.emit('msg', {'response': 'Holaaaaaaaaa'})

@sio.event
async def disconnect():
    print("I'm disconnected!")

async def main():
    await sio.connect('http://localhost:8080')
    await sio.emit('msg', {'response': 'Holaaaaaaaaa'})
    await sio.wait()

if __name__ == '__main__':
    asyncio.run(main())

