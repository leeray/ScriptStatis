#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
import re
import time, datetime
import sys

_encoding = 'utf-8'
_errors='ignore'
loger = None

data_statictis = {}
_tmp_list = []

group_name_wap = ['ip', 'time', 'method', 'url', 'status', 'log_9', 'cookieinfo']
matchs_wap=ur'^([\d.]+) \S+ \S+ \[\d\d/\w\w\w/\d\d\d\d:(\d\d):\d\d:\d\d \+0800\] "(GET|POST|PUT|HEAD|DELETE) (.*?) .*?" (\d{3}) .*? ".*?" "(.*?)" ".*?" ".*?" "(.*?)"'
compiles_wap=re.compile(matchs_wap)

def wap_Statictis(parent, filename):
    obj_file = {}
    sta_total = 0
    sta_num = 0
    _tmp_list = []
    f = codecs.open(os.path.join(parent, filename), 'r', encoding=_encoding, errors=_errors)
    row = f.readline()

    while row:
         
        jsonb = {}
        sta_total = sta_total + 1
           
        data_match=compiles_wap.search(row)
        if data_match :
            sta_num = sta_num + 1
            pass
        else:
            print row
               
        row = f.readline()
    
    
    print "total:{0}  statis_num:{1}".format(str(sta_total),str(sta_num))

                
if __name__ == '__main__':
    wap_Statictis('/opt/logs/nginx/3g.youku.com/access', 'log.20111110')
