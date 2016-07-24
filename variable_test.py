#!/usr/bin/python
#

class TestClass:
    def __init__ (self):
        testValue = "A"
        print "Point 1: %s" % (testValue)
        try:
            testValue = "B"
            fo = open("config_devices.xml")
            print "Point 2: %s" % (testValue)
            print "File status: %s" % (fo.closed)
        except IOError:
            testValue = "C"
            print "Point 3: %s" % (testValue)
        finally:
            testValue = "D"
            if (not fo.closed):
                fo.close()
        
        print "File status: %s" % (fo.closed)
        print "Point 4: %s" % (testValue)    

tc = TestClass()