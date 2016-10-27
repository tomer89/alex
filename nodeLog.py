# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 10:35:25 2016

@author: user
"""

from suspects import suspects

class nodeLog:
    ts = ""
    uid = ""
    id_orig_address = ""
    id_orig_port = ""
    id_resp_address = ""
    id_resp_port = ""
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
    request_header_len	= ""
    response_header_len = ""
    insights_adnet_name = ""
    insights_ad_type= ""
    insights_impressions = ""
    insights_clicks = ""
    adnet = ""
    ip_host_used_a_lot = False
    host_contains_ad = False
    uri_contains_ad = False
    percent_diff_referrers = 0.0
    
    def __init__(self , loglist):
        self.ts = loglist[0]
        self.uid = loglist[1]
        self.id_orig_address = loglist[2]
        self.id_orig_p = loglist[3]
        self.id_resp_address = loglist[4]
        self.id_resp_p = loglist[5]
        self.trans_depth = loglist[6]
        self.method = loglist[7]
        self.host = loglist[8]
        self.uri = loglist[9]
        self.referrer = loglist[10]
        self.version = loglist[11]
        self.user_agent = loglist[12]
        self.request_body_len = loglist[13]
        self.response_body_len = loglist[14]
        self.status_code = loglist[15]
        self.status_msg = loglist[16]
        self.info_code = loglist[17]
        self.info_msg = loglist[18]
        self.filename = loglist[19]
        self.tags = loglist[20]
        self.username = loglist[21]
        self.password = loglist[22]
        self.proxied = loglist[23]
        self.orig_fuids = loglist[24]
        self.orig_mime_types = loglist[25]
        self.resp_fuids = loglist[26]
        self.resp_mime_types = loglist[27]
        self.location = loglist[28]
        self.request_header_len = loglist[29]
        self.response_header_len = loglist[30]
        self.insights_adnet_name = loglist[31]
        self.insights_ad_type= loglist[32]
        self.insights_impressions = loglist[33]
        self.insights_clicks = loglist[34]
        self.adnet = loglist[35]
        
    def get(self, value):
        if value is "id_resp_address":
            return self.id_resp_address