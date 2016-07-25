#!/usr/bin/python

import xml.sax

class XMLDevice:
    def __init__(self):
        self.tag = ""
        self.category = ""
        self.name = ""
        self.loc = ""
        self.code = ""
        self.desc = ""
        self.connected = ""
        self.addr_i2c = ""
        self.addr_port = ""
        
    def printSelf(self):
        print("\n====================")
        print "Tag: %s, Category: %s" % (self.tag, self.category)
        print "           Name: ", self.name
        print "       Location: ", self.loc
        print "    Description: ", self.desc
        print "           Code: ", self.code
        print "     Connected?: ", self.connected
        print "  Address, Port: %s, %s" % (self.addr_i2c, self.addr_port) 

class XMLDeviceHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.name = ""
        self.loc = ""
        self.code = ""
        self.desc = ""
        self.connected = ""
        self.addr_i2c = ""
        self.addr_port = ""
        
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        print "startElement: Tag: %s, Attributes: %s" % (tag, attributes)
        if tag == "panel":
            print "=========Panel========="
            category = attributes["category"]
            print "    Category: ", category
            self.createDevice(tag, category)
        elif tag == "holoprojector":
            print "=====Holoprojector====="
            category = attributes["category"]
            print "    Category: ", category
            self.createDevice(tag, category)
            
    def createDevice(self, tag, category):
        newDevice = XMLDevice()
        newDevice.tag = tag
        newDevice.category = category
        deviceList.append(newDevice)

    def endElement(self, tag):
        print "endElement: Tag: ", tag 
        currentDevice = deviceList[len(deviceList) - 1]
        if self.CurrentData == "name":
            print "        Name: ", self.name
            currentDevice.name = self.name
        elif self.CurrentData == "loc":
            print "    Location: ", self.loc
            currentDevice.loc = self.loc
        elif self.CurrentData == "desc":
            print " Description: ", self.desc
            currentDevice.desc = self.desc
        elif self.CurrentData == "code":
            print "        Code: ", self.code
            currentDevice.code = self.code
        elif self.CurrentData == "connected":
            print "   Connected: ", self.connected
            currentDevice.connected = self.connected
        elif self.CurrentData == "addr_i2c":
            print " Address i2c: ", self.addr_i2c
            currentDevice.addr_i2c = self.addr_i2c
        elif self.CurrentData == "addr_port":
            print "Address port: ", self.addr_port
            currentDevice.addr_port = self.addr_port
        self.CurrentData = ""

    def characters(self, content):
        print "characters: Content: ", content
        if self.CurrentData == "name":
            self.name = content
        elif self.CurrentData == "loc":
            self.loc = content
        elif self.CurrentData == "desc":
            self.desc = content
        elif self.CurrentData == "code":
            self.code = content
        elif self.CurrentData == "connected":
            self.connected = content
        elif self.CurrentData == "addr_i2c":
            self.addr_i2c = content
        elif self.CurrentData == "addr_port":
            self.addr_port = content

deviceList = []

if (__name__ == "__main__"):
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    Handler = XMLDeviceHandler()
    parser.setContentHandler(Handler)
    parser.parse("config_devices.xml")
    print "\n\n"
    print "Found %d devices." % (len(deviceList))
    print "\n"
    for device in deviceList:
        device.printSelf()
