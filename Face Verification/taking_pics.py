import numpy as np
import cv2
import time
from math import floor

cap =  cv2.VideoCapture(0)
faceC = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
sampleNo = 1
while (True):

    ret, img=cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceC.detectMultiScale(gray, 1.3,5)
    for (x,y,w,h) in faces:
        
        roi = img[y:y+h, x:x+w]
        
        
        cv2.imwrite("Dataset/User1." + str(sampleNo)+".jpg", roi)
        print(x, y, w, h)
    #cv2.imshow('img_taking', img)
    cv2.waitKey(500)
    sampleNo = sampleNo+1
    if (sampleNo>20):
        break
cap.release()
cv2.destroyAllWindows()

    