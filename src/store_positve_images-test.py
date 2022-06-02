import unittest
import os
import cv2

class store_positive_images(unittest.TestCase):
    def test_comprobarPathNoexiste(self):
        path = 'C:\pruebaVV'  # comprueba dentro de la ruta
        crearcarpeta = False
        if not os.path.exists(f"{path}/pos/"):  # devuelve true o false
            os.makedirs(f"{path}/pos/")
            crearcarpeta = True
            print("La carpeta fue creada")
        self.assertTrue(crearcarpeta)  # comprueba

    def test_comprobarPathExiste(self):
        path = 'C:\pruebaVV'  # comprueba dentro de la ruta
        if os.path.exists(f"{path}/pos/"):  # devuelve true o false
            crearcarpeta = False
            print("La carpeta ya existe")
        self.assertFalse(crearcarpeta)  # comprueba

    # 2do caso

    def test_comprobarlistArchivo(self):

        path = 'C:\pruebaImgPos'  # comprueba dentro de la ruta
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            print(img_path)
            img_orginal = cv2.imread(img_path)
            cv2.imshow("imagen Cargada", img_orginal)
            assert (img_path == "C:\\pruebaImgPos\\gun.jpg")  # comprueba que lista los archivos de la carpeta

    def test_RedimensionarImg(self):

        path = 'C:\pruebaImgPos'  # comprueba dentro de la ruta
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            print(img_path)
            img_orginal = cv2.imread(img_path)
            alto, ancho = img_orginal.shape[:2]  # funcoonqueobtieneanchioyalto de la imagen
            print(alto)
            print(ancho)
            img_redimensionar = cv2.resize(img_orginal, (400, 350))
            altoR, anchoR = img_redimensionar.shape[:2]
            print(altoR)
            print(anchoR)
            cv2.imwrite(f"{path}/" + str(1) + ".jpg", img_redimensionar)
            assert (img_path == "C:\\pruebaImgPos\\gun.jpg")  # comprueba que lista los archivos de la carpeta


if __name__ == '__main__':
    unittest.main()
