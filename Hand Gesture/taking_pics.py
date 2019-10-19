import numpy as np
import cv2
import time

cap =  cv2.VideoCapture(0)
faceC = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
sampleNo = 1
while (True):

    ret, img=cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceC.detectMultiScale(gray, 1.3,5)
    for (x,y,w,h) in faces:
        cv2.imwrite("Dataset/User1." + str(sampleNo)+".jpg", img)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('img_taking', img)
    cv2.waitKey(500)
    sampleNo = sampleNo+1
    if (sampleNo>20):
        break
cap.release()
cv2.destroyAllWindows()

    