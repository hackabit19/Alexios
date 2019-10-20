import dbus
import numpy as np
import cv2
import time
import os
from sourav_helper1 import checkCall
import sys
print("ppp")
cap =  cv2.VideoCapture(0)
fist_cascade = cv2.CascadeClassifier('fist.xml')
palm_cascade = cv2.CascadeClassifier('palm_v4.xml')

bus = dbus.SystemBus()

manager = dbus.Interface(bus.get_object('org.ofono', '/'),
                        'org.ofono.Manager')

modems = manager.GetModems()

for path, properties in modems:
    #print "[ %s ]" % (path)
    #print("Currently in check_call_first.py")

    if "org.ofono.VoiceCallManager" not in properties["Interfaces"]:
        continue

    mgr = dbus.Interface(bus.get_object('org.ofono', path),
                    'org.ofono.VoiceCallManager')
    
    calls = mgr.GetCalls()
    
    for path, properties in calls:
        state = properties["State"]
        #print "[ %s ] %s" % (path, state)
        call = dbus.Interface(bus.get_object('org.ofono', path),
                        'org.ofono.VoiceCall')

def hang_up():
    modem = modems[0][0]
    print("Currently in hangup_all_calls.py..... hanging")
    if (len(sys.argv) == 2):
        modem = sys.argv[1]

    mgr = dbus.Interface(bus.get_object('org.ofono', modem),
                            'org.ofono.VoiceCallManager')

    mgr.HangupAll()



def recieve_call():
    for path, properties in calls:
            state = properties["State"]
            #print "[ %s ] %s" % (path, state)
            #print("Currently in answer_calls.py")

            if state != "incoming":
                #print("No Incoming calls!")
                continue
            call.Answer()


def check_for_signal():
    ct = time.time()
    while (True):
	
        ret, img=cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #print("Currently in incoming_call.py")
        fists = fist_cascade.detectMultiScale(gray, 1.3, 5)
        palms = palm_cascade.detectMultiScale(gray, 1.3, 5)
        cv2.imshow('img', img)
        # Accept
        for (x,y,w,h) in fists:
            #cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            #cv2.imshow('img',img)
            #cap.release()
            #cv2.destroyAllWindows()
            return 1
        # Decline:
        for (x,y,w,h) in palms:
            #cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            #cv2.imshow('img',img)
            #cap.release()
            #cv2.destroyAllWindows()
            return 0
            
        if (time.time() - ct >10):
	    os.system("python sourav_helper1.py")
	    if(checkCall()==0):
            	return 0
            ct = time.time()
        cv2.waitKey(5)

def check_for_stop_signal():
    ct = time.time()
    while (True):
	
        ret, img=cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #print("Currently in incoming_call.py")
        fists = fist_cascade.detectMultiScale(gray, 1.3, 5)
        palms = palm_cascade.detectMultiScale(gray, 1.3, 5)
        cv2.imshow('img', img)

        # Decline:
        for (x,y,w,h) in palms:
            #cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            #cv2.imshow('img',img)
            #cap.release()
            #cv2.destroyAllWindows()
            return 0
        if (time.time() - ct>3):
	    os.system("python sourav_helper1.py")
	    if(checkCall()==0):
            	return 0
            ct = time.time()
        cv2.waitKey(5)
        

if __name__ == "__main__":

    print("Check if there is an incoming call:")
    print("sss")

    os.system("python sourav_helper1.py")
    if(checkCall):
        print("Now there is a call, so we need to ask what to do:")
	if(check_for_signal()):
            print("the user has given fist:")
            recieve_call()
            print("Now that we have recived a call, we need to know if the call is still active:")
            if(check_for_stop_signal()==0): 
    	        print("the call has been cut or is demanded to be cut")
    	        hang_up()
            	print("hung now")
            	
        else:
            print("the user wants to reject the call:")
	    hang_up()