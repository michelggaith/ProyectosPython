#Proyecto con uso de camara 
import cv2 as cv

capturaVideo = cv.VideoCapture(0)
if not capturaVideo.isOpened():
    print("No se encontro camara")
    exit()
while True:
    tipoCamara,Camara=capturaVideo.read()
    grises = cv.cvtColor(Camara, cv.COLOR_BGR2GRAY)
    cv.imshow("En vivo: ", Camara)
    if cv.waitKey(1) == ord("q"):
        break
capturaVideo.release()
cv.destroyAllWindows()
