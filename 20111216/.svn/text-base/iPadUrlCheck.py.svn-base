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
pid = sys.argv[1]

group_name_api = ['ip', 'time', 'method', 'url', 'arg_get', 'arg_post', 'status', 'log_9']
matchs_api=ur'^([\d.]+) \"\d\d\d\d-\d\d-\d\dT(\d\d):\d\d:\d\d\+08:00\" (GET|POST|PUT|HEAD|DELETE) "(.*?)" "(.*?)" "(.*?)" (\d{3}) .*? .*? "(.*?)"'
compiles_api=re.compile(matchs_api)

#match_ver =  ur'ver=\d[.]+[\d|.]*\d&'
#match_oper = ur'operator=([^&A-Z]+)&'
#match_os_ver = ur'os_ver=\d[.]+[\d|.]*\d&'
#match_brand = ur'brand=([^&A-Z]+)&'
#match_btype = ur'btype=([^&A-Z]+)&'
#match_os = ur'os=([^&A-Z0-9]+)&'
#match_network = ur'network=([^&A-Z]+)&'
match_ver =  ur'ver=\d[.]+[\d|.]*\d&'
match_oper = ur'operator=([^&]+)&'
match_os_ver = ur'os_ver=\d[.]+[\d|.]*\d&'
match_brand = ur'brand=([^&]+)&'
match_btype = ur'btype=([^&]+)&'
match_os = ur'os=([^&]+)&'
match_network = ur'network=([^&]+)&'

compiles_os = re.compile(match_os)
compiles_oper = re.compile(match_oper)
compiles_ver = re.compile(match_ver)
compiles_os_ver = re.compile(match_os_ver)
compiles_brand = re.compile(match_brand)
compiles_btype = re.compile(match_btype)
compiles_network = re.compile(match_network)

url_2_1 = ur'/openapi-wireless/(get|add|send|search|login|verifyUser|doRegister)'
url_2_2 = ur'(/layout/mtk|/layout/apple|/openapi-cms/android|/internal|/ctrl)'
compiles_url_1=re.compile(url_2_1)
compiles_url_2=re.compile(url_2_2)

def ipad_check(parent, filename):
    obj_file = {}
    sta_total = 0
    sta_num = 0
    _tmp_list = []
    f = codecs.open(os.path.join(parent, filename), 'r', encoding=_encoding, errors=_errors)
    f.seek(0, os.SEEK_END)

    while True:
        row = f.readline()
        if not row:
            time.sleep(10)
            continue
        if 'pid={0}'.format(pid) not in row:
            continue
        #print row
        jsonb = {}
        sta_total = sta_total + 1
        
        data_match=compiles_api.search(row)
        if data_match :
            jsonb.update(dict(zip(group_name_api, data_match.groups())))
            
            if not jsonb.get('url',''):
                print "#Null Url# "
            elif compiles_url_1.search(jsonb.get('url','')) or compiles_url_2.search(jsonb.get('url','')) :
                print "#Call 2.0 Url# "
            else:
                pass
            
            arg_get = jsonb.get('arg_get','')
            if arg_get :
                qs = arg_get.split('&')
                qs = [x.split('=') for x in qs]
                qs = [('arg_' + y[0], y[1]) for y in qs if len(y) == 2]
                jsonb.update(dict(qs))
            
            arg_post = jsonb.get('arg_post','')
            if arg_post :
                qs = arg_post.split('&')
                qs = [x.split('=') for x in qs]
                qs = [('arg_' + y[0], y[1]) for y in qs if len(y) == 2]
                jsonb.update(dict(qs))
            
            args = '{0}&{1}'.format(arg_get, arg_post)
            
            if not compiles_ver.search(args) :
                print ur'#ver# not define! '
            
            if not compiles_oper.search(args) :
                print ur'#operator# not define! '
            
            if not compiles_network.search(args) :
                print ur'#network# not define! '
            
            if 'initial' in jsonb.get('url',''):
                if not compiles_os.search(args) :
                    print ur'#os# not define! '
                
                if not compiles_os_ver.search(args):
                    print ur'#os_ver# not define! '
                
                if not compiles_brand.search(args):
                    print ur'#brand# not define! '
                
                if not compiles_btype.search(args):
                    print ur'#btype# not define! '
            print row
            sta_num = sta_num + 1
        else:
            print "ERROR Log:{0}".format(row)
               
        row = f.readline()
    
    
    print "total:{0}  statis_num:{1}".format(str(sta_total),str(sta_num))


def ipad_check_source(stime,etime):
    obj_file = {}
    sta_total = 0
    sta_num = 0
    _tmp_list = []
    f = codecs.open(os.path.join(parent, filename), 'r', encoding=_encoding, errors=_errors)
    row = f.readline()

    while row:
        
        jsonb = {}
        sta_total = sta_total + 1
        
        data_match=compiles_api.search(row)
        if data_match :
            sta_num = sta_num + 1
            pass
        else:
            print row
               
        row = f.readline()
    
    
    print "total:{0}  statis_num:{1}".format(str(sta_total),str(sta_num))

if __name__ == '__main__':
    ipad_check('/opt/logs/nginx/statis/', 'ae9da0087ccd38cd_log')
