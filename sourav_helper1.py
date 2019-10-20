import dbus
import numpy as np
import cv2
import time
import sys
from sourav_helper2 import setCallStatus 
print("checking if there's a call")

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

def checkCall():
    for paths, properties in calls:
        state = properties["State"]
        if state == "incoming":
            return 1
        else:
            return 0