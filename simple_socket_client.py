#!/usr/bin/python
#
# Simple Python Socket Client app
#

import socket                   # Import the socket module

s = socket.socket ()            # Create the socket object 's'
host = socket.gethostname()     # Get the local machine name
port = 12345                    # The port to communicate on

s.connect((host, port))         # Attempt to make the connection
print s.recv(1024)              # Read in 1024 bytes and print them
s.close                         # Close the socket connection

# End of Simple Python Socket Client app