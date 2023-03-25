import cv2
import numpy as np

imagen = cv2.imread('monedassoles.jpg')
ValorGauss = 15
ValorKernel =21
#CONVERSION A GRISES
grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
#Suavizado de ruido
gauss = cv2.GaussianBlur(grises, (ValorGauss, ValorGauss), 0)
canny = cv2.Canny(gauss, 60, 100)
kernel = np.ones((ValorKernel, ValorKernel), np.uint8)
cierre = cv2.morphologyEx(canny,cv2.MORPH_CLOSE, kernel)
contorno,jerarquia =cv2.findContours(cierre.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Monedas encontradas: {}".format(len(contorno)))

cv2.drawContours(imagen, contorno, -1, (251,60,50),3)
#MOSTRAR IMAGEN
cv2.imshow('Original', imagen)
#cv2.imshow('Grises', grises)
#cv2.imshow('Umbral', umbral)

cv2.waitKey(0)
cv2.destroyAllWindows()
