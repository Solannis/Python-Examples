#!/usr/bin/python
#
# Python Class Socket Client app
#

import socket                   # Import the socket module
import threading                # Import the threading module

#global_host = "raspberrypi_b"
global_host = "MitchelRetina5K"
global_port = 49152


class ClientSocket:
    'ClientSocket class to represent client connection service'
    
    def __init__(self, hostName, portNumber):
        self.clientSocket = socket.socket()
#        self.hostName = socket.gethostname()
#        self.hostName = "raspberrypi_b"
        self.hostName = hostName
        self.hostPort = portNumber
        print "Host Name: ", self.hostName
        print "Host Port: ", self.hostPort
        
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