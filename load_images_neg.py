import urllib.request
import cv2 as cv
import numpy as np
import os

guns = []
dirp = r'/mnt/d/Development'
dir = r'/mnt/d/Development/positivesimages'
for i in os.listdir(dir):
    guns.append(i)
print(guns)

features = []
labels = []

gun_cascade = cv.CascadeClassifier('cascade2.xml')


# 5, 2 , 7

def store_raw_images():
    pic_num = 1
    path = dir
    if not os.path.exists(f"{path}/neg/"):
        os.makedirs(f"{path}/neg/")

    for img in os.listdir(path):
        try:
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            print(path)
            print("img_path" + img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            resized_image = cv.resize(gray, (100, 100))

            cv.imwrite(f"{path}/neg/" + str(pic_num) + ".jpg", resized_image)
            pic_num += 1
        except Exception as e:
            print(str(e))
    print("OPERACION REALIZADA CORRECTAMENTE, IMAGENES GUARDADAS Y CONVERTIDAS A BLANCO Y NEGRO")
    # gun_rect = gun_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

    # for (x,y,w,h) in gun_rect:
    #    guns_roi = gray[y:y+h, x:x+w]
    #    features.append(guns_roi)
    #    labels.append(label)


def store_positive_images():
    pic_num = 1
    path = dirp
    if not os.path.exists(f"{path}/pos/"):
        os.makedirs(f"{path}/pos/")

    for img in os.listdir(path):
        try:
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            print(path)
            print("img_path" + img_path)

            resized_image = cv.resize(img_array, (400, 350))

            cv.imwrite(f"{path}/pos/" + str(pic_num) + ".jpg", resized_image)
            pic_num += 1
        except Exception as e:
            print(str(e))
    print("OPERACION REALIZADA CORRECTAMENTE, IMAGENES GUARDADAS")


def create_pos_n_pos(path):
    try:
        for file_type in [path + '/pos']:
            for img in os.listdir(file_type):
                if file_type == path + '/pos':
                    line = file_type + '/' + img + '\n'
                    with open('positives.txt', 'a') as f:
                        f.write(line)
        print("¡FELICIDADES, INFO.DAT GENERADO CON EXITO !")
    except:
        return None


def create_pos_n_neg():
    path = dir
    for file_type in [path + '/neg']:
        for img in os.listdir(file_type):

            if file_type == path + '/pos':
                line = file_type + '/' + img + ' 1 0 0 50 50\n'
                with open('info.dat', 'a') as f:
                    f.write(line)
            elif file_type == path + '/neg':
                line = file_type + '/' + img + '\n'
                with open('negatives.txt', 'a') as f:
                    f.write(line)
    print("¡FELICIDADES, BG.TXT GENERADO CON EXITO !")


def find_uglies():
    match = False
    for file_type in [dir + '/neg']:
        for img in os.listdir(file_type):
            for ugly in os.listdir('uglies'):
                try:
                    current_image_path = str(file_type) + '/' + str(img)
                    ugly = cv.imread('uglies/' + str(ugly))
                    question = cv.imread(current_image_path)
                    if ugly.shape == question.shape and not (np.bitwise_xor(ugly, question).any()):
                        print('That is one ugly pic! Deleting!')
                        print(current_image_path)
                        os.remove(current_image_path)
                except Exception as e:
                    print(str(e))


store_raw_images()
store_positive_images()
# create_pos_n_pos()
# create_pos_n_neg()
# print(f'Imagenes nuevas ingresadas = {len(features)}')
# print(f'Labels nuevos = {len(labels)}')
