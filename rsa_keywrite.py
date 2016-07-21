#!/usr/bin/python

import rsa

(pubkey, privkey) = rsa.newkeys(512)
print pubkey
print privkey

out_data = pubkey.save_pkcs1('PEM')
writeFile = open("pubkey_test.pem", "w")
writeFile.write(out_data)
writeFile.close()
print "Key written"