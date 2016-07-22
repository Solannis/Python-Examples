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
import rsa                      # Import the RSA Python module

global_host = ""
global_port = 12345
global_configSystemFile = "config_system.xml"
global_configDevicesFile = "config_devices.xml"
global_clientKeyFilePublic = "ClientKey_public.PEM"
global_clientKeyFilePrivate = "ClientKey_private.PEM"
global_serverKeyFilePublic = "ServerKey_public.PEM"

#
# Thought process:
#
# 1) Check for keys:
#   If keys are absent, go on to step 2.
#   If keys are present, go on to step 3.
#
# 2) Generate and store keys.
#   Go on to step 4
#
# 3) Load keys.
# 
# 4) Load system configuration XML file.
# 
# 5) Set up socket connection.
#
# 6) Start chatting with server.
#

class KeyManager:
    #
    # Initialization function
    #
    def __init__(self):
        self.clientKeyPublic = ""
        self.clientKeyPrivate = ""
        self.serverKeyPublic = ""
        self.clientKeyPublicExists = False
        self.clientKeyPrivateExists = False
        self.serverKeyPublicExists = False
        self.keyReadMode = "r"

    #
    # Check for the presense of the client's public key
    #
    def ClientPublicKeyCheck(self):
        keyPresent = False
        try:
            readFile = open(global_clientKeyFilePublic, self.keyReadMode)
            readFile.close()
            print "Public client key found."
            keyPresent = True
        except IOError:
            print "Public client key missing."
        return keyPresent

    #
    # Check for the presence of the client's private key
    #
    def ClientPrivateKeyCheck(self):
        keyPresent = False
        try:
            readFile = open(global_clientKeyFilePrivate, self.keyReadMode)
            readFile.close()
            print "Private client key found."
            keyPresent = True
        except IOError:
            print "Private client key missing."
        return keyPresent

    #
    # Check for the presence of the server's public key
    #
    def ServerPublicKeyCheck(self):
        keyPresent = False
        try:
            readFile = open(global_serverKeyFilePublic, "r")
            readFile.close()
            print "Public server key found."
            allKeysFound = True
        except IOError:
            print "Public server key missing."
        return keyPresent
        
    #
    # Check for the presence of all keys
    #
    def KeyCheck(self):
        allKeysFound = False
        self.clientKeyPublicExists = self.ClientPublicKeyCheck()
        self.clientKeyPrivateExists = self.ClientPrivateKeyCheck()
        self.serverKeyPublicExists = self.ServerPublicKeyCheck()
        if ((self.clientKeyPublicExists == True) and (self.clientKeyPrivateExists == True) and (self.serverKeyPublicExists == True)):
            allKeysFound = True
        return allKeysFound
        
    #
    # Client Key Generator
    #
    # Decision process:
    # If Private:True and Public:True, there is no need to generate keys.
    # If Private:True and Public:False, generate a new public key from the private one.
    # If Private:False and Public:True, generate both keys new.
    # If Private:False and Public:False, generate both keys new.
    #

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


km = KeyManager()
if (km.KeyCheck() == False):
    print "False"
else:
    print "True"

#cs = ClientSocket(global_host, global_port)
#cs.ClientStart()

# End of Python Class Socket Client app