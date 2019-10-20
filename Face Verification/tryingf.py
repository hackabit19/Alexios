import cv2
import time
cap = cv2.VideoCapture(0)
st = time.time()
print("here")
while(True):
    _, img =  cap.read()
    if (time.time()-st>10):
        break
    cv2.waitKey(1)
    cv2.imshow('ss', img)

cap.release()
cv2.releaseAllWindows()
    