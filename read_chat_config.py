#!/usr/bin/python

import xml.sax

class ServerConfig:
    def __init__(self):
        self.serverName = ""
        self.listenerPort = 0

    def ToString(self):
        self.string = "Server Name: %s" % (self.serverName)
        self.string = self.string + "\nListener Port: %d" % (self.listenerPort)
        return self.string

class ClientConfig:
    def __init__(self):
        self.clientName = ""
        self.serverPort = 0

    def ToString(self):
        self.string = "Client Name: %s" % (self.clientName)
        self.string = self.string + "\nServer Port: %d" % (self.serverPort)
        return self.string

class XMLConfigHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.sc = ServerConfig()
        self.cc = ClientConfig()
        
    def startElement(self, tag, attributes):
        self.CurrentData = tag
            
    def endElement(self, tag):
        self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == "servername":
            self.sc.serverName = content
        elif self.CurrentData == "listenerport":
            self.sc.listenerPort = int(content)
        elif self.CurrentData == "clientname":
            self.cc.clientName = content
        elif self.CurrentData == "serverport":
            self.cc.serverPort = int(content)

class ConfigParser:
    def __init__(self):
        self.parser = None
        self.Handler = None
        
    def ParseConfig(self):
        self.parser = xml.sax.make_parser()
        self.parser.setFeature(xml.sax.handler.feature_namespaces, 0)
        self.Handler = XMLConfigHandler()
        self.parser.setContentHandler(self.Handler)
        self.parser.parse("config_chat.xml")

#
# NOTE: NEED CODE TO DEAL WITH CORRUPTED/PARTIAL/INVALID CONFIGURATION FILE
#


""""
if (__name__ == "__main__"):
    cp = ConfigParser()
    cp.ParseConfig()
    print "\n\n"
    print cp.Handler.sc.ToString()
    print cp.Handler.cc.ToString()
"""
