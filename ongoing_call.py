def ongoing_call():
    # return 1 to hangup, 0 to  do nothing
    import numpy as np
    import cv2
    import time
    from check_call import check
    from hangup_all_calls import hangup
    from check_call_first import checkfirst

    cap =  cv2.VideoCapture(0)
    
    
    #fist_cascade = cv2.CascadeClassifier('fist.xml')
    palm_cascade = cv2.CascadeClassifier('palm_v4.xml')
    
    #start_time = time.time()
    
    while (True):
        if (check()==0): #function_name_will_change
            cap.release()   
            cv2.destroyAllWindows()
            checkfirst()
            return 0   
        ret, img=cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        #fists = fist_cascade.detectMultiScale(gray, 1.3, 5)
        palms = palm_cascade.detectMultiScale(gray, 1.3, 5)
            
        '''for (x,y,w,h) in fists:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            #cv2.imshow('img',img)
            cap.release()
            cv2.destroyAllWindows()
            return 1'''
            
            
            
        cv2.imshow('img', img)
        for (x,y,w,h) in palms:
            #cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            #cv2.imshow('img',img)
            cap.release()
            cv2.destroyAllWindows()
            hangup()
            return 1
        cv2.waitKey(150)

#print(what_to_do_with_ongoing_call())