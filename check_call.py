#!/usr/bin/python
#Python2

import dbus

def check():
    bus = dbus.SystemBus()

    manager = dbus.Interface(bus.get_object('org.ofono', '/'),
                            'org.ofono.Manager')

    modems = manager.GetModems()

    for path, properties in modems:
        print "[ %s ]" % (path)

        if "org.ofono.VoiceCallManager" not in properties["Interfaces"]:
            continue

        mgr = dbus.Interface(bus.get_object('org.ofono', path),
                        'org.ofono.VoiceCallManager')
        
        calls = mgr.GetCalls()
        
        for path, properties in calls:
            state = properties["State"]
            print "[ %s ] %s" % (path, state)

            if state == "incoming":
                return 1
            else:
                return 0

if __name__ == "__main__":
    check()
