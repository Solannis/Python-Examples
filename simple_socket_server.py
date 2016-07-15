#!/usr/bin/python
#
# Simple Python Socket Server app
#

import socket                   # Import the socket module

s = socket.socket ()            # Create the socket object 's'
host = socket.gethostname()     # Get the local machine name
port = 12345                    # The port to listen on
s.bind((host, port))            # Bind the socket to the hostname and port

s.listen(5)                     # Start listening to the port for incoming connections
while True:
    c, addr = s.accept()        # Establish a connection with the client
    print 'Received connection request from ', addr
    c.send('Thank you for connecting')
    c.close()                   # Close the connection