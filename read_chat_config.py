#!/usr/bin/python

import xml.sax

class ServerConfig:
    def __init__(self):
        self.serverName = ""
        self.listenerPort = 0

    def ToString(self):
        self.string = "Server Name: ", self.serverName
        self.string = self.string + "\nListener Port: " + str(self.listenerPort)
        return self.string

class ClientConfig:
    def __init__(self):
        self.clientName = ""
        self.serverPort = 0

    def ToString(self):
        self.string = "Client Name: ", self.clientName
        self.string = self.string + "Server Port: " + str(self.serverPort)
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
        print "[" + content + "]"
        if self.CurrentData == "servername":
            self.sc.serverName = content
        elif self.CurrentData == "listenerport":
            self.sc.listenerPort = int(content)
        elif self.CurrentData == "clientname":
            self.cc.clientName = content
        elif self.CurrentData == "serverport":
            self.cc.serverPort = int(content)

if (__name__ == "__main__"):
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    Handler = XMLConfigHandler()
    parser.setContentHandler(Handler)
    parser.parse("config_chat.xml")
    print "\n\n"
    print Handler.sc.ToString()
    print Handler.cc.ToString()
