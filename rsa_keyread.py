#!/usr/bin/python

import rsa

readFile = open("pubkey_test.pem", "r")
in_data = readFile.read()
readFile.close()
print "Key read"
pubkey = rsa.PublicKey.load_pkcs1(in_data, 'PEM')
print pubkey