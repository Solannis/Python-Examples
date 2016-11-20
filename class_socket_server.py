#!/usr/bin/python
#
# Python Class Socket Server app
#

import socket                   # Import the socket module
import threading                # Import the threading module

#
# Define some global variables
#
global_host = ""                # Detaulf global host name
global_port = 49152             # Default global host port nubmer (to listen on)
global_connections = 5          # Default global connection count (how many simultaneous connections are allowed)

class ServerSocket:
    'SocketServer class to represent server/listener functionality'
    
    #
    # Initialization Method
    #
    def __init__(self, hostName, portNumber, connectionCount):
        self.serverSocket = socket.socket()         # Create socket object, assign it to variable
        self.hostName = socket.gethostname()        # Get hostname from the socket, assign it to variable
        self.hostPort = portNumber                  # Get port nubmer argument, assign it to variable
        self.connections = connectionCount          # Get connection count argument, assign it to variable
        print "Hostname: ", self.hostName
        print "Hostport: ", self.hostPort
        print "Connects: ", self.connections

    #
    # Start the server
    #
    def ServerStart(self):
        self.serverSocket.bind((self.hostName, self.hostPort))  # Bind the socket to a port
        self.serverSocket.listen(self.connections)  # Turn on listening on that socket
        print '\n=========='
        print "Server: Started listening on host [%s] on port [%d]" % (self.hostName, self.hostPort)
    
    #
    # Listen for and accept new incoming connections
    #
    def ServerAccept(self):
        self.threadCount = 1
        while True:
            print 'Server: Waiting for new incoming connection'
            self.connectedSocket, self.connectedAddress = self.serverSocket.accept()
            print 'Server: Accepting new incoming conneciton'
            ch = ConnectionHandler(self.threadCount, self.connectedSocket, self.connectedAddress)
            ch.start()
            self.threadCount += 1
            
class ConnectionHandler (threading.Thread):
    'ConnectionHandler class to represent how connections are handled'
        
    def __init__(self, threadID, socket, address):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.connectedSocket = socket
        self.connectedAddress = address
        self.connectionID = "Connection Handler Thread [%d]:" % self.threadID
        print '----------'
        print "%s connected" % self.connectionID
        self.SendMessage()
        
    def SendMessage(self):
        print "%s sending message to client" % self.connectionID
        self.connectedSocket.send('Thank you for connecting.')
        self.connectedSocket.close()
        print "%s connection closed" % self.connectionID

ss = ServerSocket(global_host, global_port, global_connections)
ss.ServerStart()
ss.ServerAccept()
