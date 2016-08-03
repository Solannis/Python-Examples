#!/usr/bin/python
#
#   Repository: Python Examples
#    Component: New XML Test
#      Version: 0.1
# Date Created: 03-Aug-2016 MBF
# Date Updated: 
#
# 03-Aug-2016
#   Trying a new way to read and write XML via etree/ElementTree functionality within Python.
#

import xml.etree.ElementTree as ElementTree

class XMLRead:
    def __init__(self):
        self.configFile = "config_chat.xml"
        self.configTree = None
        self.configRoot = None
        self.parameters = {}
    
    def ReadConfig(self):
        self.configTree = ElementTree.parse(self.configFile)
        self.configRoot = self.configTree.getroot()
        #
        # Because I know what I am looking for (or at), I can make certain assumptions about
        # what the configuration XML file should and should not have. 
        #
        # I know that the root should have three children, and those three children should be:
        #   master, remote, client
        # and I know that each of those three children should have three children of their own:
        #   hostname, hostport, hostkeyfile
        #
        # Any missing child can be defaulted and written back out to the file.
        #
        for child in self.configRoot:
            for grandchild in child:
                keyName = child.tag + "_" + grandchild.tag
                self.parameters[keyName] = grandchild.text
        return self.parameters
        
class CheckConfiguration:
    def __init__(self):
        self.parameters = {}
        
    def CheckConfig(self, parameters):
        self.parameters = parameters
        if (self.parameters.has_key('master_hostname') == False):
            self.parameters['master_hostname'] = "Fred"
        if (self.parameters.has_key('master_hostport') == False):
            self.parameters['master_hostport'] = 50000
        if (self.parameters.has_key('master_hostkeyfile') == False):
            self.parameters['master_hostport'] = "ServerKey_private.PEM"
        if (self.parameters.has_key('rempte_hostname') == False):
            self.parameters['remote_hostname'] = "Barney"
        if (self.parameters.has_key('remote_hostport') == False):
            self.parameters['remote_hostport'] = 50001
        if (self.parameters.has_key('remote_hostkeyfile') == False):
            self.parameters['remote_hostport'] = "ServerKey_public.PEM"
        if (self.parameters.has_key('client_hostname') == False):
            self.parameters['client_hostname'] = "Wilma"
        if (self.parameters.has_key('client_hostport') == False):
            self.parameters['client_hostport'] = 50002
        if (self.parameters.has_key('client_hostkeyfile') == False):
            self.parameters['client_hostport'] = "ClientKey_public.PEM"

***** Working here
            

if __name__ == "__main__":
    xmlReader = XMLRead()
    configTree = xmlReader.ReadConfig()
    xmlShower = XMLShow()
    xmlShower.ShowConfig(configTree)


"""
print root[0].attrib
print root[1]

for child in root[0]:
    print child

"""