# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 17:26:53 2016

@author: user
"""
from log import Log

class LogsReader:

    rawTxt = ""
    txtDevidedInLines = []
    fullOopLogs = []
    oopLogs = []
    

    def __init__(self, filename):
         file = open(filename, 'r')
         self.rawTxt = file.read()
         self.txtDevidedInLines = self.rawTxt.splitlines()
         self.init_fullOop()
         self.define_oop()
         
    def init_fullOop(self):
        for i in self.txtDevidedInLines[10:]:
            string_log = i.split()
            self.fullOopLogs.append(Log(string_log,0))
            
    def define_oop(self):
        for i in self.fullOopLogs:
            if i.adnet == "none" or i.adnet == "-":
                self.oopLogs.append(Log(i,1))
         
x = LogsReader("short_log.txt")
j = 10
