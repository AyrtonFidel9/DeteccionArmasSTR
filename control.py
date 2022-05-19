import base64
import datetime
import cv2
import imutils

def transmitirVideo(frame):
    imagen = cv2.imencode('.jpg', frame)[1].tobytes()
    imagen = base64.encodebytes(imagen).decode("utf-8")
    return imagen

def emitirSIO(sio, frame):
    sio.emit('livestream', transmitirVideo(frame))
    sio.sleep(0)

def n_guns(sio, gun, frame):
    if len(gun) > 0:
        sio.emit('msg', True)
        print(datetime.datetime.now())
        sio.sleep(0)
        emitirSIO(sio, frame)
        print("guns detected " + str(len(gun)) + f"{gun}")


def detectar_arma(sio):
    gun_cascade = cv2.CascadeClassifier('cascade.xml')

    camera = cv2.VideoCapture(0)
    # camera = cv2.VideoCapture(0)
    # camera = cv2.VideoCapture(1)
    # camera = cv2.VideoCapture('data/people.mp4')

    # initialize the first frame in the video stream
    firstFrame = None

    # loop over the frames of the video

    while True:
        (grabbed, frame) = camera.read()

        # if the frame could not be grabbed, then we have reached the end of the video
        if not grabbed:
            break

        # resize the frame, convert it to grayscale, and blur it
        frame = imutils.resize(frame, width=500)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        gun = gun_cascade.detectMultiScale(gray, 1.3, 5, minSize=(100, 100))

        for (x, y, w, h) in gun:
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]

            # if the first frame is None, initialize it
        if firstFrame is None:
            firstFrame = gray
            continue

        # draw the text and timestamp on the frame
        cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                    (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

        # show the frame and record if the user presses a key
        cv2.imshow('SecurityFeed', frame)

        n_guns(sio, gun, frame)

        key = cv2.waitKey(1) & 0xFF

    # cleanup the camera and close any open windows
    camera.release()
    cv2.destroyAllWindows()

