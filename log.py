# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Log:
    time = ""
    uid = ""
    orig_h = ""       
    orig_p = ""      
    resp_h = ""      
    resp_p = ""     
    trans_depth = ""   
    method = ""
    host = ""
    uri = ""   
    referrer = ""        
    version = ""
    user_agent = ""      
    request_body_len = ""       
    response_body_len = ""   
    status_code = ""
    status_msg = ""
    info_code = "" 
    info_msg = ""  
    filename = ""   
    tags = ""
    username = ""       
    password = ""   
    proxied = ""
    orig_fuids = ""    
    orig_mime_types = "" 
    resp_fuids = ""
    resp_mime_types = "" 
    location = ""       
    request_header_len = ""      
    response_header_len = "" 
    insights_adnet_name = ""
    insights_ad_type = ""       
    insights_impressions = ""   
    insights_clicks = ""
    adnet = ""
    
    def __init__(self, log ,status):
        if status == 0:
            if len(log) is 52:
                print(log)
            self.time = log[0]
            self.uid = log[1]
            self.orig_h = log[2]    
            self.orig_p = log[3]
            self.resp_h = log[4]
            self.resp_p = log[5]
            self.trans_depth = log[6]  
            self.method = log[7]
            self.host = log[8]
            self.uri = log[9]
            self.referrer = log[10]      
            self.version = log[11]
            self.user_agent = log[12] 
            self.request_body_len = log[13]     
            self.response_body_len = log[14]
            self.status_code = log[15]
            self.status_msg = log[16]
            self.info_code = log[17]
            self.info_msg = log[18]
            self.filename = log[19]
            self.tags = log[20]
            self.username = log[21]   
            self.password = log[22]
            self.proxied = log[23]
            self.orig_fuids = log[24]
            self.orig_mime_types = log[25]
            self.resp_fuids = log[26]
            self.resp_mime_types = log[27]
            self.location = log[28]
            self.request_header_len = log[29]      
            self.response_header_len = log[30]
            self.insights_adnet_name = log[31]
            self.insights_ad_type = log[32]
            self.insights_impressions = log[33]
            self.insights_clicks = log[34]
            self.adnet = log[35]
        
        if status == 1 :
            self.time = log.time
            self.uid = log.uid
            self.orig_h = log.orig_h    
            self.orig_p = log.orig_p
            self.resp_h = log.resp_h
            self.resp_p = log.resp_p
            self.trans_depth = log.trans_depth  
            self.method = log.method
            self.host = log.host
            self.uri = log.uri
            self.referrer = log.referrer     
            self.version = log.version
            self.user_agent = log.user_agent 
            self.request_body_len = log.request_body_len     
            self.response_body_len = log.response_body_len
            self.status_code = log.status_code
            self.status_msg = log.status_msg
            self.info_code = log.info_code
            self.info_msg = log.info_msg
            self.filename = log.filename
            self.tags = log.tags
            self.username = log.username   
            self.password = log.password
            self.proxied = log.proxied
            self.orig_fuids = log.orig_fuids
            self.orig_mime_types = log.orig_mime_types
            self.resp_fuids = log.resp_fuids
            self.resp_mime_types = log.resp_mime_types
            self.location = log.location
            self.request_header_len = log.request_header_len  
            self.response_header_len = log.response_header_len
            self.insights_adnet_name = log.insights_adnet_name
            self.insights_ad_type = log.insights_ad_type
            self.insights_impressions = log.insights_impressions
            self.insights_clicks = log.insights_clicks
            self.adnet = log.adnet