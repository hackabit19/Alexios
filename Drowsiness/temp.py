from imutils import face_utils
from scipy.spatial import distance as dist
import pygame #For playing sound

pygame.mixer.init()
pygame.mixer.music.load('C:/Users/HP/Documents/GitHub/Alexios/Drowsiness/beep-01a.wav')

#import numpy as np

#import imutils
import dlib
import cv2
temp1=0
temp2=0
count=0
blink=0
sleep=0
ear=0
str="ALERT!!!"
def EAR(eye):

    A= dist.euclidean(eye[1],eye[5]) + dist.euclidean(eye[2],eye[4])
    B= dist.euclidean(eye[0],eye[3])
    C= A/2*B
    return C


cap =  cv2.VideoCapture(1)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
ear=1
while (True):

    ret, image=cap.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    rects = detector(gray, 1)
    (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
    (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
    ear = 1 
    for (i, rect) in enumerate(rects):

        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        '''
        eye1 = shape[36:42,:]
        eye2 = shape[42:48,:]
        '''
            
        eye1 = shape[lStart:lEnd]
        eye2 = shape[rStart:rEnd]
        ear = 1
        ear1 = EAR(eye1)
        ear2 = EAR(eye2)
        ear = (ear1 + ear2)/2.0

        (x, y, w, h) = face_utils.rect_to_bb(rect)
        ear = ear*100 / (h*w)

        #cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)


        #cv2.putText(image, "Face #{}".format(i + 1), (x - 5, y - 5),
        #cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
        cv2.putText(image, " {:.3f}".format(ear), (x - 25, y - 25),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)

        leftEyeHull = cv2.convexHull(eye1)
        rightEyeHull = cv2.convexHull(eye2)
        #cv2.drawContours(image, [leftEyeHull], -1, (0, 255, 0), 1)
        #cv2.drawContours(image, [rightEyeHull], -1, (0, 255, 0), 1)
        '''
        for (x, y) in shape:
            cv2.circle(image, (x, y), 1, (0, 0, 255), -1)
        '''
        break
    if (ear<=0.7):
        count=count +1
    if (ear>0.7):
        count=0
        pygame.mixer.music.stop()
        sleep =0
    if (count>1):
        blink = blink +1
        count = 0
        sleep=sleep+1
    if (sleep>=4):
        cv2.putText(image, "ALERT!!", (50, 100),
        cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0 ,0), 5)
        if(pygame.mixer.music.get_busy()==0):
            pygame.mixer.music.play(start = pygame.mixer.music.get_pos())
            
            




    #cv2.putText(image, "Blink {}".format(blink), (30,30),
    #cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)




    cv2.imshow("Output", image)
    if (cv2.waitKey(1) & 0xFF== ord("q")):
        break
cap.release()
cv2.destroyAllWindows()













































