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

import os                       # Import the OS module
import rsa                      # Import the RSA Python module
import socket                   # Import the socket module
import sys                      # Import the system module
import threading                # Import the threading module
import xml.sax                  # Import the XML reading module

global_host = ""
global_port = 12345
global_configSystemFile = "config_system.xml"
global_configDevicesFile = "config_devices.xml"

#
# Client Startup Process
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
        self.clientKeyPublic = None
        self.clientKeyPrivate = None
        self.serverKeyPublic = None
        self.clientKeyPublicExists = False
        self.clientKeyPrivateExists = False
        self.serverKeyPublicExists = False
        self.keyFormat = "PEM"
        self.keyReadMode = "r"
        self.keyWriteMode = "w"
        self.keyTypeClient = "Client"
        self.keyTypeServer = "Server"
        self.keyClassPublic = "Public"
        self.keyClassPrivate = "Private"
        self.clientKeyFilePublic = "ClientKey_public.PEM"
        self.clientKeyFilePrivate = "ClientKey_private.PEM"
        self.serverKeyFilePublic = "ServerKey_public.PEM"

    #
    # Check for the presense of the client's public key
    #
    def ClientPublicKeyCheck(self):
        #
        # Had to dig into this a bit. Was getting an error regarding the var
        # readFile being called (where I perform readFile.close() function)
        # before the var had been defined in the first place. In the code,
        # I defined readFile at the readFile = open(...) function, but if
        # Python hits an exception upon opening (e.g. no file found to open)
        # in the first place, the var is not created at all, and there is
        # no way I can find to create an empty file object (e.g. no way to
        # file = new FileObject() from within Python).
        #
        # This all came about by trying to make sure the file object was
        # closed even in the event of an exception. The issue is that if
        # the file object cannot be opened, no object exists to be closed
        # in the first place. This meant a restructure of my code. There
        # were two ways to do this:
        #
        # 1) Create a readFile object with a value of None and compare
        #       against that. If it is None, there is nothing to close. If
        #       it is not None, it is probably closeable.
        # 2) Go with the fact that if the file was not openable, I don't
        #       need to worry about closing it later on. This will lead
        #       to faster, smaller, more efficient code. So this is what
        #       I am doing.
        #
        keyPresent = False
        try:
            readFile = open(self.clientKeyFilePublic, self.keyReadMode)
            readFile.close()
            keyPresent = True
        except IOError:
            print "ClientPublicKeyCheck: No public client key found."
        return keyPresent

    #
    # Check for the presence of the client's private key
    #
    def ClientPrivateKeyCheck(self):
        keyPresent = False
        try:
            readFile = open(self.clientKeyFilePrivate, self.keyReadMode)
            readFile.close()
            keyPresent = True
        except IOError:
            print "ClientPrivateKeyCheck: No private client key found."
        return keyPresent

    #
    # Check for the presence of the server's public key
    #
    def ServerPublicKeyCheck(self):
        keyPresent = False
        try:
            readFile = open(self.serverKeyFilePublic, self.keyReadMode)
            readFile.close()
            keyPresent = True
        except IOError:
            print "ServerPublicKeyCheck: No public server key found."
        return keyPresent
        
    #
    # Check for the presence of keys, determine next steps.
    #
    def KeyCheck(self):
        #
        # Check each key to see whether it is present or not.
        #
        self.clientKeyPublicExists = self.ClientPublicKeyCheck()
        self.clientKeyPrivateExists = self.ClientPrivateKeyCheck()
        self.serverKeyPublicExists = self.ServerPublicKeyCheck()

        #
        # Now check the Client Private and Public keys to see what needs to be done.
        #
        # Decision process:
        # If Private:True and Public:True, there is no need to generate keys.
        # If Private:True and Public:False, generate a new public key from the private one.
        # If Private:False and Public:True, generate both keys new.
        # If Private:False and Public:False, generate both keys new.
        #
        if (self.clientKeyPrivateExists) and (self.clientKeyPublicExists):
            #
            # Both keys are present. Load the keys into objects.
            #
            print "KeyCheck: Private key is present. Public key is present. Loading existing keys."
            self.clientKeyPrivate = self.KeyLoad(self.clientKeyFilePrivate, self.keyTypeClient, self.keyClassPrivate)
            self.clientKeyPublic = self.KeyLoad(self.clientKeyFilePublic, self.keyTypeClient, self.keyClassPublic)
        elif (self.clientKeyPrivateExists) and (self.clientKeyPublicExists == False):
            #
            # Private key exists, but the public key is missing. Regenerate the
            # public key from the private key's data.
            #
            print "KeyCheck: Private key is present. Public key is missing. Regenerating public key."
            self.clientKeyPrivate = self.KeyLoad(self.clientKeyFilePrivate)
            self.clientKeyPublic = rsa.key.PublicKey(self.clientKeyPrivate.n, self.clientKeyPrivate.e)
            self.KeySave(self.clientKeyPublic, self.clientKeyFilePublic, self.keyTypeClient, self.keyClassPublic)
        elif (self.clientKeyPublicExists) and (self.clientKeyPrivateExists == False):
            #
            # Private key is missing, but the public key exists. Since we cannot
            # regenerate the private key from the public key, create a new set of
            # both keys: private and public.
            #
            print "KeyCheck: Private key is missing. Public key is present. Generating new key pair."
            os.remove(self.keyClientFilePublic)
            self.KeyGen()
        else:
            #
            # Both the private and public keys are missing. Generate a new pair
            # of keys.
            #
            print "KeyCheck: Private key is missing. Public key is missing. Generating new key pair."
            self.KeyGen()
            
    def KeyLoad(self, keyFile, keyType, keyClass):
        try:
            readFile = open(keyFile, self.keyReadMode)
            key_data = readFile.read()
            readFile.close()
        except IOError:
            print "KeyLoad: Error while loading %s %s key." % (keyType, keyClass)
            return None
        if (keyClass == "Private"):
            loadedKey = rsa.PrivateKey.load_pkcs1(key_data, self.keyFormat)
        elif (keyClass == "Public"):
            loadedKey = rsa.PublicKey.load_pkcs1(key_data, self.keyFormat)
        else:
            print "KeyLoad: Unknown key class requested. No %s key was loaded." % (keyClass)
            return None
        print "KeyLoad: %s %s key loaded." % (keyType, keyClass)
        return loadedKey

    def KeySave(self, keyData, keyFile, keyType, keyClass):
        try:
            writeFile = open(keyFile, self.keyWriteMode)
            key_data = keyData.save_pkcs1(self.keyFormat)
            writeFile.write(key_data)
            writeFile.close()
            print "KeySave: %s %s key saved." % (keyType, keyClass)
        except IOError:
            print "KeySave: Error while saving %s %s key. No key was saved." % (keyType, keyClass)
        finally:
            return
        
    def KeyGen(self):
        (keyPub, keyPriv) = rsa.newkeys(512)
        print "KeyGen: New keys generated."
        self.clientKeyPrivate = keyPriv
        self.clientKeyPublic = keyPub
        self.KeySave(self.clientKeyPrivate, self.clientKeyFilePrivate, self.keyTypeClient, self.keyClassPrivate)
        self.KeySave(self.clientKeyPublic, self.clientKeyFilePublic, self.keyTypeClient, self.keyClassPublic)
        print "KeyGen: New keys saved successfully."

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
km.KeyCheck()
print km.clientKeyPublic

#cs = ClientSocket(global_host, global_port)
#cs.ClientStart()

# End of Python Class Socket Client app