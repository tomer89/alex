# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 10:59:18 2016

@author: user
"""
from reader import fullLog
import numpy as np
import copy

class counters:
    local_logs = []
    arrange_by_response_id = []
    list_of_ip_counts = []
    list_of_counts_of_ip = []
    list_of_ips_above_num = []  
    host_ip_repititians_barrier = 2
    
    
    def __init__(self , fulllog):
        self.local_logs = fulllog
        self.index_list_most_used_ip()
        
        
    def index_list_most_used_ip(self):
        """this is important for knowing how many clients go to every ip"""
        
        unique, counts = np.unique(self.local_logs.all_id_resp_address, return_counts=True)
        np.asarray((unique, counts)).T

        
        self.list_of_ip_counts = unique
        self.list_of_counts_ip = counts
       
        self.host_ip_repititians_barrier = np.median(counts) - 1
        list_of_count_indexs = list(np.where(counts > self.host_ip_repititians_barrier))[0]
        
        print("size of list_of_count_indexs (amount of unique ips above barrier) is: " + str(len(list_of_count_indexs)))
        counter = 0
        for i in list_of_count_indexs:
            for j in self.local_logs.logsByValue(unique[i],"id_resp_address"):
                self.list_of_ips_above_num.append(j)
                if (j.adnet == "none" or j.adnet == "-"):
                    j.ip_host_used_a_lot = True
                    counter += 1
                
         

    def host_contains_ad(self):
        """checks if the word "ad" is in the host name """
        for log in self.local_logs.allNone:
            if ("ad" in log.host) and ("load" not in log.host and "radio" not in log.host):
                log.host_contains_ad = True
    
    def uri_contains_ad(self):
        """checks if the word "ad" is in the uri """
        for log in self.local_logs.allNone:
            if ("ad" in log.uri):
                log.uri_contains_ad = True
                
        
                
    def amount_of_referrers(self):
        tmp_referrers = []
        tmp_ip_host =""    
        full_list = self.list_of_ips_above_num
        for index, ip_host in enumerate(full_list):
            same_ip_list = self.local_logs.logsByValue(ip_host,"id_resp_address")#.referrer          
            for log in same_ip_list:
                if log.referrer not in tmp_referrers:
                    tmp_referrers.append(log.referrer)
                    
            for log in same_ip_list:
                log.percent_diff_referrers = (len(tmp_referrers)/len(same_ip_list))
                # i need to erase from the full list
            tmp_referrers = []
                
            
        
        
         
        tmp_referrers = []
        added_to_all_logs = True
        first = False
        percent = 0.0
        number_of_ips = 0
        number_of_diff_ips = 0
        self.local_logs.allReferrers()
        for index1,ip_host in enumerate(self.list_of_ips_above_num):
            if first:
                tmp_referrers = []
                index_of_first = index1
                tmp_host = ip_host
                tmp_referrers.append((self.local_logs.logsByValue(ip_host,"id_resp_address").referrer))
                tmp_referrers()
                first = False
            else:
                tmp_referrers.append((self.local_logs.logsByValue(ip_host,"id_resp_address").referrer))
            if log.referrer not in tmp_referrers:
                if added_to_all_logs == False:
                    for index2, log in enumerate(self.list_of_ips_above_num, start=index_of_first):
                        if index2 != index_of_last:
                            log.percent_diff_referrers = percent
                        else:
                            added_to_all_logs = True
                            tmp_referrers = []
                            break
                else:
                    if first:
                        index_of_first = index1
                        first = False                        
                    if log.referrer not in tmp_referrers:
                        po =9
                            
                        
        
        
        

        
        
    def response_header_len():
        print("didnt do nothing")
        
      
      
      
fulllog = fullLog("short_log.txt")

listLog = fulllog.listLog
allLogs = fulllog.listoflists
shineFound = fulllog.shineFound
allNone = fulllog.allNone
oopList = fulllog.oopList

nrg = counters(fulllog)
jjj = np.asarray(nrg.local_logs.all_id_resp_address)
nrg.uri_contains_ad()
nrg.host_contains_ad()
count = 0 
for i in nrg.list_of_ips_above_num:
    if(i.host_contains_ad == True and i.uri_contains_ad):     
       # print(i.host + "\"")
        count += 1
check1 = nrg.local_logs.logsByValue("66.235.148.64","id_resp_address")
check2 = nrg.local_logs.logsByValue("stats.adobe.com","host")

#nrg.amount_of_referrers()


#for i in value:
#    print(nrg.local_logs.oopList[i].host)
print("did last")


