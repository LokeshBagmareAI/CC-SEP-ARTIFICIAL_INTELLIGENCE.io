#Project Name - Face Detection
#projectee Name - Lokesh Bagmare
#Role - Artificial Intelligence Intern

#Script
#importing CV2 Library
import cv2
import numpy as np

#uploading xml files
cascade_face = cv2.CascadeClassifier('C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')

#In the above line of code the path of \ xml sheet is given by me according to my System. U have to change the Path according to ur system 

#giving access to the camera
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    print(ret)

    #coverting out bgr to grayscale color
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    f = cascade_face.detectMultiScale(grey, 1.3,4)
 
    for (x,y,w,h) in f: 
        cv2.rectangle(img, (x,y), (x + w, y + h), (0,255,0),4)

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()