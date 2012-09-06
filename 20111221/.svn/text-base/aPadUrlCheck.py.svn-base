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
#pid = sys.argv[1]

group_name_api = ['ip', 'time', 'method', 'url', 'arg_get', 'arg_post', 'status', 'log_9']
matchs_api=ur'^([\d.]+) \"\d\d\d\d-\d\d-\d\dT(\d\d):\d\d:\d\d\+08:00\" (GET|POST|PUT|HEAD|DELETE) "(.*?)" "(.*?)" "(.*?)" (\d{3}) .*? .*? "(.*?)"'
compiles_api=re.compile(matchs_api)

match_ver =  ur'ver=\d[.]+[\d|.]*\d&'
match_oper = ur'operator=([%a-zA-Z][^&]+)&'
match_os_ver = ur'os_ver=\d[.]+[\d|.]*\d&'
match_brand = ur'brand=([^&]+)&'
match_btype = ur'btype=([^&]+)&'
match_os = ur'os=([%a-zA-Z][^&]+)&'
match_network = ur'network=([%a-zA-Z][^&]+)&'

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
        #if 'pid={0}'.format(pid) not in row:
        #    continue
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
            if 'ver=' in args:
                if not compiles_ver.search(args) :
                    print ur'##ver## invalid parameter! '
            else:
                print ur'##ver## not define! '
            
            if 'operator=' in args:
                if not compiles_oper.search(args) :
                    print ur'##operator## invalid parameter!'
            else :
                print ur'##operator## not define! '
            
            if 'network=' in args:
                if not compiles_network.search(args):
                    print ur'##network## invalid parameter! '
            else :
                print ur'##network## not define! '
            
            
            if 'initial' in jsonb.get('url',''):
                if 'os=' in args:
                    if not compiles_os.search(args) or 'os=null&' in args :
                        print ur'##os## invalid parameter! '
                else :
                    print ur'##os## not define! '
                    
                if 'os_ver=' in args:
                    if not compiles_os_ver.search(args):
                        print ur'##os_ver## invalid parameter! '
                else:
                    print ur'##os_ver## not define! '
                
                if 'brand=' in args:
                    if not compiles_brand.search(args) or 'brand=null&' in args:
                        print ur'##brand## invalid parameter! '
                else:
                    print ur'##brand## not define! '
                
                if 'btype=' in args:
                    if not compiles_btype.search(args) or 'btype=null&' in args:
                        print ur'##btype## invalid parameter! '
                else:
                    print ur'##btype## not define! '
            print row
            sta_num = sta_num + 1
        else:
            print "ERROR Log:{0}".format(row)
    
    
    print "total:{0}  statis_num:{1}".format(str(sta_total),str(sta_num))

if __name__ == '__main__':
    ipad_check('/opt/logs/nginx/statis/', '0bf8f9f8a3c904c0_log')
