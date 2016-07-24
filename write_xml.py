#!/usr/bin/python
#

class ServerSection:
    def __init__(self):
        self.section = "server"
        self.serverName = ["servername", "MitchelRetina5K"]
        self.serverKeyPublic = ["serverkey_public", "ABCD1234"]
        self.listenerPort = ["listenerport", 12345]
        self.tab = "    "

    def ToString(self):
        self.string = self.tab + "<%s>\n" % (self.section)
        self.string = self.string + self.tab + self.tab + "<%s>%s</%s>\n" % (self.serverName[0], self.serverName[1], self.serverName[0])
        self.string = self.string + self.tab + self.tab + "<%s>%s</%s>\n" % (self.serverKeyPublic[0], self.serverKeyPublic[1], self.serverKeyPublic[0])
        self.string = self.string + self.tab + self.tab + "<%s>%s</%s>\n" % (self.listenerPort[0], self.listenerPort[1], self.listenerPort[0])
        self.string = self.string + self.tab + "</%s>" % (self.section)
        return self.string

class ClientSection:
    def __init__(self):
        self.section = "client"
        self.clientName = ["clientname", "MitchelRetina5K"]
        self.clientKeyPublic = ["clientkey_public", "WXYZ6789"]
        self.serverPort = ["serverport", 12345]
        self.tab = "    "
    
    def ToString(self):
        self.string = self.tab + "<%s>\n" % (self.section)
        self.string = self.string + self.tab + self.tab + "<%s>%s</%s>\n" % (self.clientName[0], self.clientName[1], self.clientName[0])
        self.string = self.string + self.tab + self.tab + "<%s>%s</%s>\n" % (self.clientKeyPublic[0], self.clientKeyPublic[1], self.clientKeyPublic[0])
        self.string = self.string + self.tab + self.tab + "<%s>%s</%s>\n" % (self.serverPort[0], self.serverPort[1], self.serverPort[0])
        self.string = self.string + self.tab + "</%s>" % (self.section)
        return self.string

class ChatConfig:
    def __init__(self):
        self.xmlVersionString = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
        self.section = "chatconfig"
        self.ss = ServerSection()
        self.cs = ClientSection()
    
    def ToString(self):
        self.string = self.xmlVersionString + "\n"
        self.string = self.string + "<%s>\n" % (self.section)
        self.string = self.string + self.ss.ToString() + "\n"
        self.string = self.string + self.cs.ToString() + "\n"
        self.string = self.string + "</%s>\n" % (self.section)
        return self.string

#cc = ChatConfig()
#print cc.ToString()


