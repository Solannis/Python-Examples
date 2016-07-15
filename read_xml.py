#!/usr/bin/python

import xml.sax

class PanelHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.name = ""
        self.loc = ""
        self.desc = ""
        self.connected = ""
        self.addr_i2c = ""
        self.addr_port = ""
        
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "panel":
            print "=====Panel====="
            category = attributes["category"]
            print "    Category: ", category

    def endElement(self, tag):
        if self.CurrentData == "name":
            print "        Name: ", self.name
        elif self.CurrentData == "loc":
            print "    Location: ", self.loc
        elif self.CurrentData == "desc":
            print " Description: ", self.desc
        elif self.CurrentData == "connected":
            print "   Connected: ", self.connected
        elif self.CurrentData == "addr_i2c":
            print " Address i2c: ", self.addr_i2c
        elif self.CurrentData == "addr_port":
            print "Address port: ", self.addr_port
        self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == "name":
            self.name = content
        elif self.CurrentData == "loc":
            self.loc = content
        elif self.CurrentData == "desc":
            self.desc = content
        elif self.CurrentData == "connected":
            self.connected = content
        elif self.CurrentData == "addr_i2c":
            self.addr_i2c = content
        elif self.CurrentData == "addr_port":
            self.addr_port = content

if (__name__ == "__main__"):
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    Handler = PanelHandler()
    parser.setContentHandler(Handler)
    parser.parse("config.xml")