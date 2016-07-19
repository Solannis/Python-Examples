#!/usr/bin/python
#
# CLI Test
#

import sys

global_prompt = "-> "

class CLI_Capture:
    'Class which operates the CLI function'
    
    def __init__(self, prompt):
        self.prompt = prompt
        self.command = ""
    
    def StartCLI(self):
        while True:
            self.command = raw_input(self.prompt)
            parser = CLI_Parser(self.command)
            parser.ParseCommand()


class CLI_Parser:
    'Class which parses the CLI commands captured'
    
    def __init__(self, command):
        self.command = command
    
    def ParseCommand (self):
        self.command = self.command.lower()
        if (self.command == "exit") or (self.command == "quit"):
            sys.exit()

cmdLine = CLI_Capture(global_prompt)
cmdLine.StartCLI()
