import cv2
print(cv2.__version__)
imagen = cv2.imread('contorno.jpg')
#CONVERSION A GRISES
grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
_,umbral = cv2.threshold(grises, 100, 255, cv2.THRESH_BINARY)
contorno,jerarquia =cv2.findContours(umbral,cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagen, contorno, -1, (251,60,50),3)
#MOSTRAR IMAGEN
cv2.imshow('Original', imagen)
#cv2.imshow('Grises', grises)
#cv2.imshow('Umbral', umbral)

cv2.waitKey(0)
cv2.destroyAllWindows()
