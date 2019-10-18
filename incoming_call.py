
def incoming_call():
    
    import numpy as np
    import cv2
    import time
    from check_call import check
    from answer_calls import answer_call
    cap =  cv2.VideoCapture(1)
    
    
    fist_cascade = cv2.CascadeClassifier('fist.xml')
    palm_cascade = cv2.CascadeClassifier('palm_v4.xml')
    
    start_time = time.time()
    
    while (True):
        if(check()==0):
            return 0
        ret, img=cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        fists = fist_cascade.detectMultiScale(gray, 1.3, 5)
        palms = palm_cascade.detectMultiScale(gray, 1.3, 5)
        #cv2.imshow('img', img)
        for (x,y,w,h) in fists:
            #cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            #cv2.imshow('img',img)
            cap.release()
            cv2.destroyAllWindows()
            answer_call()
            return 1
            
            
            
        
        for (x,y,w,h) in palms:
            #cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            #cv2.imshow('img',img)
            cap.release()
            cv2.destroyAllWindows()
            return 0
                

        cv2.waitKey(150)
        
        if (time.time() - start_time>45):
            return 0

#print(incoming_call())
        

