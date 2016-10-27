# -*- coding: utf-8 -*-
"""
Created on Sun Aug 07 22:49:46 2016

@author: user
"""

from nodeLog import nodeLog 
import numpy as np        



class fullLog:
    listLog = []  
    listoflists = []
    allNone = []
    shineFound = []
    oopList = []
    all_id_resp_address = []
    all_host = []
    all_response_len = []
    none_id_resp_address = []
    none_host = []
    all_referrers = []
    amount_of_not_oopable = 0
    
    
    def __init__(self, txt):
        self.readingList(txt)
        self.logtolistoflists()
        self.createOOP()
        self.shineFound()        
        self.allNone()
        self.allIdRespAddress()


        
    def readingList(self, txt):
        """reading txt to raw list of lines"""
        with open(txt) as f:
            f = f.readlines()
        self.listLog = f

        
    def logtolistoflists(self):
        """from list of lines"""
        for line in self.listLog:
            tmpLine = line.strip('\n').split("\t")
            if len(tmpLine) > 30 and len(tmpLine) < 37:
                self.listoflists.append(tmpLine)
            else:
                self.amount_of_not_oopable = self.amount_of_not_oopable + 1
            
                
    def createOOP(self):
        i = 0
        for log in self.listoflists:
            if len(log) is 36:
                self.oopList.append(nodeLog(log))
                i += 1
        
    def shineFound(self):
        temp = []
        for line in self.oopList: 
            if (line.adnet != "none") and (line.adnet != "generic"):
                temp.append(line)
        self.shineFound = temp
        
        
    def allNone(self):
        temp = []
        for line in self.oopList:
            if (line.adnet == "none"):
                temp.append(line)
        self.allNone = temp
        
    def allReferrers(self):
        for log in self.oopList:
            self.all_referrers.append(log.referrer)
            
    def allIdRespAddress(self):
        ooplist = self.oopList
        for log in ooplist:
            self.all_id_resp_address.append(log.id_resp_address)
            if log.adnet is "none" or log.adnet is "-":
                self.none_id_resp_address.append(log.id_resp_address)
                
    def allHosts(self):
        ooplist = self.oopList
        for log in ooplist:
            self.all_host.append(log.host)
            if log.adnet is "none" or log.adnet is "-":
                self.none_host(log.host)
                
    def allResponseLen(self):
        oopList = self.oopList
        for log in ooplist:
            self.all_response_len(log.response_header_len)
        
    
        
    """converts the value given from the form of _from to the form of _to"""
    def translater(self, value ,_from, _to):
        if _from is "id_resp_address":
            index = self.all_id_resp_address.index(value)
            return self.oopList[index].get(_to)
           
    def logsByValue(self, value, _type):
        if _type is "id_resp_address":
            log_list = []
            np_resp_address = list(np.where(np.asarray(self.all_id_resp_address) == value))[0]
            for index in np_resp_address:
                log_list.append(self.oopList[index])
            return log_list
        if _type is "host":
            log_list = []
            np_host = list(np.where(np.asarray(self.all_host) == value))[0]
            for index in np_host:
                log_list.append(self.oopList[index])
            return log_list

 
