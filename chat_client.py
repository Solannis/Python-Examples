#!/usr/bin/python
#
# Python Chat Client app
#
# This application is a simple socket chat client. It merges the functionality
# of the class-centric socket client, advanced XML reader, and CLI examples 
# created earlier.
#
# Version 0.1
# Created: 18-Jul-2016 MBF
#

import socket                   # Import the socket module
import sys                      # Import the system module
import threading                # Import the threading module
import xml.sax                  # Import the XML reading module

global_host = ""
global_port = 12345
global_config_host = "config_host.xml"
global_config_devices = "config_devices.xml"

class ClientSocket:
    'ClientSocket class to represent client connection service'
    
    def __init__(self, hostName, portNumber):
        self.clientSocket = socket.socket()
        self.hostName = socket.gethostname()
        self.hostPort = portNumber
        
    def ClientStart(self):
        print '\n=========='
        print 'Client: Starting connection'
        self.clientSocket.connect((self.hostName, self.hostPort))
        print 'Client: Connection established'
        self.messageIncoming = self.clientSocket.recv(1024)
        print "Client: message received: %s" % self.messageIncoming
        self.clientSocket.close
        print 'Client: connection closed'

cs = ClientSocket(global_host, global_port)
cs.ClientStart()

# End of Python Class Socket Client app