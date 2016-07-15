#!/usr/bin/python
#
# Simple Class Test app
#

hostname = "myHostName"
hostport = 12345

class TestClass:
    'Test Class'
    def __init__(self, host, port):
        self.myhostname = host
        self.myhostport = port
        
    def displayParams(self):
        print "Host name is: %s" % self.myhostname
        print "Host port is: %d" % self.myhostport

t = TestClass(hostname, hostport)
t.displayParams()