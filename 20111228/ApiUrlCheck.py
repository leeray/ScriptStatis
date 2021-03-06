#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
import re
import time, datetime
import sys
import urllib

_encoding = 'utf-8'
_errors='ignore'
loger = None

data_statictis = {}
_tmp_list = []
pid = sys.argv[1]

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
match_guid = ur'guid=([a-z0-9][^&]+)&'
match_sessionid = ur'sessionid=([a-z0-9A-Z][^&]+)&'
match_vid = ur'vid=([a-z0-9A-Z%][^&]+)&'
match_beforeduration = ur'before_duration=([0-9^&]+)&'
match_duration = ur'&duration=([0-9^&]+)&'
match_complete = ur'complete=([01^&])&'
match_ple = ur'play_load_events=(((\d+[,]\d+)\|?)[^\|&]+)&'
match_pht = ur'play_hdsd_times=([0-9^&]+)&'
match_phd = ur'play_hdsd_duration=([0-9^&]+)&'
match_pst = ur'play_sdhd_times=([0-9^&]+)&'
match_psd = ur'play_sdhd_duration=([0-9^&]+)&'
match_link = ur'link=([%a-zA-Z][^&]+)&'
match_resptime = ur'resptime=(\d+[\.]\d\d)&'

compiles_os = re.compile(match_os)
compiles_oper = re.compile(match_oper)
compiles_ver = re.compile(match_ver)
compiles_os_ver = re.compile(match_os_ver)
compiles_brand = re.compile(match_brand)
compiles_btype = re.compile(match_btype)
compiles_network = re.compile(match_network)
compiles_guid = re.compile(match_guid)
compiles_sessionid = re.compile(match_sessionid)
compiles_vid = re.compile(match_vid)

compiles_beforeduration = re.compile(match_beforeduration)
compiles_duration = re.compile(match_duration)
compiles_complete = re.compile(match_complete)
compiles_ple = re.compile(match_ple)
compiles_pht = re.compile(match_pht)
compiles_phd = re.compile(match_phd)
compiles_pst = re.compile(match_pst)
compiles_psd = re.compile(match_psd)
compiles_link = re.compile(match_link)
compiles_resptime = re.compile(match_resptime)

url_2_1 = ur'/openapi-wireless/(get|add|send|search|login|verifyUser|doRegister)'
url_2_2 = ur'(/layout/mtk|/layout/apple|/openapi-cms/android|/internal|/ctrl)'
compiles_url_1=re.compile(url_2_1)
compiles_url_2=re.compile(url_2_2)

def api_check(parent, filename):
    obj_file = {}
    info = {}
    vv = {}
    sta_total = 0
    sta_num = 0
    _tmp_list = []
    f = codecs.open(os.path.join(parent, filename), 'r', encoding=_encoding, errors=_errors)
    #f.seek(0, os.SEEK_END)

    while True:
        row = f.readline()
        if not row:
            time.sleep(10)
            continue
        if 'pid={0}'.format(pid) not in row:
            continue
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
            
            args = '&{0}&{1}&'.format(arg_get, arg_post)
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
            else :
                if 'guid=' in args:
                    guid_match = compiles_guid.search(args)
                    if not guid_match :
                        print ur'##guid## invalid parameter!'
                    else:
                        guid = guid_match.groups()[0]
                        #info[guid] = {}
                        if not info.get(guid,''):
                            info[guid] = {}
                        if not jsonb['log_9'] :
                            print ur'##UA## invalid parameter!'
                        else:
                            if guid and info[guid].get('ua',''):
                                if info[guid]['ua'] != jsonb['log_9'] :
                                    print ur'##UA## not match!'
                            else:
                                info[guid]['ua'] = jsonb['log_9']
                        
                        if '/statis/response-time' in jsonb.get('url', ''):
                            link_match = compiles_link.search(args)
                            if not link_match:
                                print ur'##VV## invalid parameter link=? ! '
                            else:
                                print 'Link={0}'.format(urllib.unquote(link_match.groups()[0]))
                            
                            resptime_match = compiles_resptime.search(args)
                            if not resptime_match:
                                print ur'##VV## invalid parameter resptime=? ! '
                        
                        if 'statis/vv' in jsonb.get('url', ''):
                            sessionid_match = compiles_sessionid.search(args)
                            if not sessionid_match:
                                print ur'##VV## invalid parameter sessionid=? ! '
                            else:
                                sessionid = sessionid_match.groups()[0]
                            
                                vid_match = compiles_vid.search(args)
                                if not vid_match:
                                    print ur'##VV## invalid parameter vid=? ! '
                                else:
                                    vid = vid_match.groups()[0]
                                
                                    if not info[guid].get(vid, ''):
                                        info[guid][vid] = {}
                                    
                                    if 'type=begin' in args:
                                        info[guid][vid]['begin'] = sessionid
                                    elif 'type=end' in args:
                                        
                                        beforeduration_match = compiles_beforeduration.search(args)
                                        if not beforeduration_match :
                                            print ur'##VV## invalid parameter before_duration=? ! '
                                        
                                        duration_match = compiles_duration.search(args)
                                        if not duration_match :
                                            print ur'##VV## invalid parameter duration=? ! '
                                        
                                        #print duration_match.groups()[0]
                                        
                                        complete_match = compiles_complete.search(args)
                                        if not complete_match :
                                            print ur'##VV## invalid parameter complete=? ! '
                                        
                                        ple_match = compiles_ple.search(args)
                                        if not ple_match :
                                            print ur'##VV## invalid parameter play_load_events=? ! '
                                        
                                        #print ple_match.groups()[0]
                                        
                                        pht_match = compiles_pht.search(args)
                                        if not pht_match :
                                            print ur'##VV## invalid parameter play_hdsd_times=? ! '
                                        
                                        phd_match = compiles_phd.search(args)
                                        if not phd_match :
                                            print ur'##VV## invalid parameter play_hdsd_duration=? ! '
                                        
                                        pst_match = compiles_pst.search(args)
                                        if not pst_match :
                                            print ur'##VV## invalid parameter play_sdhd_times=? ! '
                                        
                                        psd_match = compiles_psd.search(args)
                                        if not psd_match :
                                            print ur'##VV## invalid parameter play_sdhd_duration=? ! '
                                        
                                        info[guid][vid]['end'] = sessionid
                                        
                                        if not info[guid][vid].get('begin', '') :
                                            print '##VV## not found type=begin!'
                                        else:
                                            if info[guid][vid]['begin'] != info[guid][vid]['end']:
                                                print '##VV## sessionid not match!'
                                        
                                        info[guid][vid]['begin'] = ''
                                        info[guid][vid]['end'] = ''   
                                    else:
                                        print '#VV# invalid parameter type=? !'
                else :
                    print ur'##guid## not define! '
                    
            print row
            sta_num = sta_num + 1
        else:
            print "ERROR Log:{0}".format(row)
    
    
    print "total:{0}  statis_num:{1}".format(str(sta_total),str(sta_num))

if __name__ == '__main__':
    #api_check('/opt/logs/nginx/access/', 'log')
    api_check('/home/leeray/Desktop/', 'log')
