import numpy as np
import cv2
import imutils
import datetime
import asyncio
import socketio
import tracemalloc


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
    await sio.emit('message', {'response': 5})


@sio.event
async def disconnect():
    print("I'm disconnected!")

async def main():
    await sio.connect('http://localhost:8080')
    await sio.emit('msg', {'response': 'Holaaaaaaaaa soy la vigilanci'})
    #await sio.wait()
    await detectar_arma()
    await sio.wait()


async def notificacion():
    #await asyncio.emit('msg', {'noti':'¡¡¡¡Arma detectada!!!!'})
    await sio.emit('msg',{'notificacion':'¡¡¡¡Arma detectada!!!!'})


async def detectar_arma():
    gun_cascade = cv2.CascadeClassifier('cascade.xml')
    camera = cv2.VideoCapture('data/gun4_2.mp4')
    #camera = cv2.VideoCapture('data/people.mp4')

    # initialize the first frame in the video stream
    firstFrame = None

    # loop over the frames of the video

    gun_exist = False
    while True:
        (grabbed, frame) = camera.read()

        # if the frame could not be grabbed, then we have reached the end of the video
        if not grabbed:
            break

        # resize the frame, convert it to grayscale, and blur it
        frame = imutils.resize(frame, width=500)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        
        gun = gun_cascade.detectMultiScale(gray, 1.3, 5, minSize = (100, 100))
        
            
        for (x,y,w,h) in gun:
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]    

        # if the first frame is None, initialize it
        if firstFrame is None:
            firstFrame = gray
            continue

        # draw the text and timestamp on the frame
        cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                        (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

        # show the frame and record if the user presses a key
        cv2.imshow('SecurityFeed',frame)

        if len(gun) > 0:
            #sio.send('¡¡¡¡Arma detectada!!!!')
            #gun_exist = True
            #notificacion()
            await sio.emit('msg',{'notificacion':'¡¡¡¡Arma detectada!!!!'})
        else:
            gun_exist = False
        
        key = cv2.waitKey(1) & 0xFF

    # cleanup the camera and close any open windows
    camera.release()
    cv2.destroyAllWindows()

    if gun_exist:
        print("guns detected "+str(len(gun))+f"{gun}")

if __name__ == '__main__': 
    tracemalloc.start()
    asyncio.run(main())




