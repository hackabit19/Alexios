#!/usr/bin/python

import sys
import dbus
from check_call_first import checkfirst

def hangup:
    bus = dbus.SystemBus()
    print("Currently in hangup_all_calls.py")
    manager = dbus.Interface(bus.get_object('org.ofono', '/'),
                            'org.ofono.Manager')

    modems = manager.GetModems()
    modem = modems[0][0]

    if (len(sys.argv) == 2):
        modem = sys.argv[1]

    manager = dbus.Interface(bus.get_object('org.ofono', modem),
                            'org.ofono.VoiceCallManager')

    manager.HangupAll()
    checkfirst()