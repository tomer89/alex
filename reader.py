# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 17:26:53 2016

@author: user
"""


class LogsReader:

    rawTxt = ""
    txtDevidedInLines = ""
    oopLogs = []
    
    def __init__(self, filename):
         file = open(filename, 'r')
         self.rawTxt = file.read()
         self.txtDevidedInLines = self.rawTxt.splitlines()
         

         
x = LogsReader("short_log.txt")
for i in x.txtDevidedInLines:
    print(i)