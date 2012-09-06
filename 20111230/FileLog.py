#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
import re
import time, datetime
import sys
import Logging as logging

_encoding = 'utf-8'
_errors='ignore'
loger = None

data_statictis = {}
_tmp_list = []

p_version = re.compile(ur'(.*?) \((.*?)\)')
p_img = re.compile(ur'(\.png|\.jpg|\.js(\?.*?)?|\.gif|\.css|\.ico)$', re.I)
p_stream = re.compile(r'/stream/')

group_name = ['ip', 'time', 'method', 'url', 'status', 'log_9']
matchs=ur'^([\d.]+) \S+ \S+ \[\d\d/\w\w\w/\d\d\d\d:(\d\d):\d\d:\d\d \+0800\] "(GET|POST|PUT|HEAD|DELETE) (.*?) .*?" (\d{3}) .*? ".*?" "(.*?)"'
compiles=re.compile(matchs)

group_name_api = ['ip', 'time', 'method', 'url', 'arg_get', 'arg_post', 'status', 'log_9']
matchs_api=ur'^([\d.]+) \"\d\d\d\d-\d\d-\d\dT(\d\d):\d\d:\d\d\+08:00\" (GET|POST|PUT|HEAD|DELETE) "(.*?)" "(.*?)" "(.*?)" (\d{3}) .*? .*? "(.*?)"'
compiles_api=re.compile(matchs_api)

group_name_wap = ['ip', 'time', 'method', 'url', 'status', 'log_9', 'cookieinfo']
matchs_wap=ur'^([\d.]+) \S+ \S+ \[\d\d/\w\w\w/\d\d\d\d:(\d\d):\d\d:\d\d \+0800\] "(GET|POST|PUT|HEAD|DELETE) (.*?) .*?" (\d{3}) .*? ".*?" "(.*?)" ".*?" ".*?" "(.*?)"'
compiles_wap=re.compile(matchs_wap)

def format_argments(jsonb):
    if not jsonb :
        return
    url = jsonb.get('url', '')
    if '?' in url and '=' in url:
        qs = url.split('?')[1].split('&')
        qs = [x.split('=') for x in qs]
        qs = [('arg_' + y[0], y[1]) for y in qs if len(y) == 2]
        jsonb.update(dict(qs))

def api_Statictis(parent, filename, targetpath):
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
            jsonb.update(dict(zip(group_name_api, data_match.groups())))
            verinfo = jsonb['log_9']
            versioninfo_match = p_version.search(verinfo)
            if versioninfo_match:
                jsonb['version'] = versioninfo_match.group(1)
                jsonb['clientinfo'] = versioninfo_match.group(2)
                del jsonb['log_9']
            
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
            
            arg_pid =  jsonb.get('arg_pid','')
            
            if arg_pid and len(arg_pid) == 16:
                filename = arg_pid
            else :
                filename = 'nopid'

            try:
                output_f = obj_file.get(filename, codecs.open(os.path.join(targetpath, filename), 'a', encoding=_encoding, errors=_errors))
            except :
                loger.error('Write File Error. targetpath: %s.  filename: %s. line:%d'  % (filename, filename, sta_total))
                row = f.readline()
                continue
                
            obj_file[filename] = output_f
            result = []
            _args = ['time','ip','url','method','status','version','clientinfo','log_9','arg_guid','arg_cid','arg_uid']
            for _arg in _args:
                result.append(jsonb.get(_arg,'#'))
            
            print >> output_f, u'^_^'.join(['{{{0}}}'.format(i) for i in range(len(result))]).format( *result )
            
            sta_num = sta_num + 1
            
            if sta_num % 10000  == 0:
                output_f.flush()
            
        row = f.readline()
    
    for a in obj_file.keys() :
        try:
            obj_file[a].close()
        except IOError:
            loger.error('IOError! obj_file[%s].close() error.'  % (a))
            continue        

    obj_file = {}
        
    loger.info("total:{0}  statis_num:{1}".format(str(sta_total),str(sta_num)))

def wap_Statictis(parent, filename, targetpath):
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
            jsonb.update(dict(zip(group_name_wap, data_match.groups())))
            
            url = jsonb['url']
            if (not url or p_img.search(url)):
                row = f.readline()
                continue

            verinfo = jsonb['log_9']
            versioninfo_match = p_version.search(verinfo)
            if versioninfo_match :
                jsonb['version'] = versioninfo_match.group(1)
                jsonb['clientinfo'] = versioninfo_match.group(2)
                del jsonb['log_9']
            
            cookie = jsonb.get('cookieinfo','')
            if cookie :
                cookielist = cookie.split(';')
                if cookielist :
                    cookiestr = cookielist[0]
                    if cookiestr :
                        if len(cookiestr) != 40 :
                            cookiestr = cookiestr.replace('\\x22','')
                            cookiestr = cookiestr.replace('\x22','')
                        jsonb['cookie'] = cookiestr
                        del jsonb['cookieinfo']                 

            filename = jsonb.get('arg_pid','nopid')
            try:
                output_f = obj_file.get(filename, codecs.open(os.path.join(targetpath, filename), 'a', encoding=_encoding, errors=_errors))
            except:
                loger.error('Write File Error. targetpath: %s.  filename: %s. line:%d'  % (filename, filename, sta_total))
                row = f.readline()
                continue
                
            obj_file[filename] = output_f
            result = []
            _args = ['time','ip','url','method','status','version','clientinfo','log_9','arg_guid','arg_cid','cookie','cookieinfo']
            for _arg in _args:
                result.append(jsonb.get(_arg,'#'))
            
            print >> output_f, u'^_^'.join(['{{{0}}}'.format(i) for i in range(len(result))]).format( *result )
            
            sta_num = sta_num + 1
            
            if sta_num % 10000  == 0:
                output_f.flush()
            
        row = f.readline()
    
    for a in obj_file.keys() :
        try:
            obj_file[a].close()
        except IOError:
            continue        

    obj_file = {}
    
    loger.info("total:{0}  statis_num:{1}".format(str(sta_total),str(sta_num)))

def go_Statictis(parent, filename, targetpath):
    obj_file={}
    sta_total = 0
    sta_num = 0
    _tmp_list = []
    f = codecs.open(os.path.join(parent, filename), 'r', encoding=_encoding, errors=_errors)
    row = f.readline()
    
    while row:
        jsonb = {}
        sta_total = sta_total + 1
        data_match=compiles.search(row)
        if data_match :
            jsonb.update(dict(zip(group_name, data_match.groups())))
            url = jsonb['url']
            if (not url or p_img.search(url) or p_stream.search(url)):
                row = f.readline()
                continue

            format_argments(jsonb)
            
            verinfo = jsonb['log_9']
            versioninfo_match = p_version.search(verinfo)
            if versioninfo_match:
                jsonb['version'] = versioninfo_match.group(1)
                jsonb['clientinfo'] = versioninfo_match.group(2)
                del jsonb['log_9']
            
            
            arg_pid =  jsonb.get('arg_pid','')
            
            if arg_pid and len(arg_pid) == 16:
                filename = arg_pid
            else :
                filename = 'nopid'
            
            try:
                output_f = obj_file.get(filename, codecs.open(os.path.join(targetpath, filename), 'a', encoding=_encoding, errors=_errors))
            except :
                loger.error('Write File Error. targetpath: %s.  filename: %s. line:%d'  % (filename, filename, sta_total))
                row = f.readline()
                continue
                
            obj_file[filename] = output_f
            result = []
            _args = ['time','ip','url','method','status','version','clientinfo','log_9','arg_guid','arg_cid']
            for _arg in _args:
                result.append(jsonb.get(_arg,'#'))
            
            print >> output_f, u'^_^'.join(['{{{0}}}'.format(i) for i in range(len(result))]).format( *result )

            sta_num = sta_num + 1
            
            if sta_num % 10000  == 0:
                output_f.flush()
            
        row = f.readline()
    
    for a in obj_file.keys() :
        try:
            obj_file[a].close()
        except IOError:
            continue        

    obj_file = {}
    
    loger.info("total:{0}  statis_num:{1}".format(str(sta_total),str(sta_num)))

def ios_Statictis(parent, filename, targetpath):
    obj_file={}
    sta_total = 0
    sta_num = 0
    _tmp_list = []
    f = codecs.open(os.path.join(parent, filename), 'r', encoding=_encoding, errors=_errors)
    row = f.readline()
    
    while row:
        jsonb = {}
        sta_total = sta_total + 1
        data_match=compiles.search(row)
        if data_match :
            jsonb.update(dict(zip(group_name, data_match.groups())))
            
            url = jsonb['url']
            if (not url or p_img.search(url)):
                row = f.readline()
                continue

            format_argments(jsonb)            
            verinfo = jsonb['log_9']
            versioninfo_match = p_version.search(verinfo)
            if versioninfo_match:
                jsonb['version'] = versioninfo_match.group(1)
                jsonb['clientinfo'] = versioninfo_match.group(2)
                del jsonb['log_9']
            
            filename = jsonb.get('arg_pid','nopid')
            try:
                output_f = obj_file.get(filename, codecs.open(os.path.join(targetpath, filename), 'a', encoding=_encoding, errors=_errors))
            except :
                loger.error('Write File Error. targetpath: %s.  filename: %s. line:%d'  % (filename, filename, sta_total))
                row = f.readline()
                continue
                
            obj_file[filename] = output_f
            result = []
            _args = ['time','ip','url','method','status','version','clientinfo','log_9','arg_guid','arg_cid']
            for _arg in _args:
                result.append(jsonb.get(_arg,'#'))
            
            print >> output_f, u'^_^'.join(['{{{0}}}'.format(i) for i in range(len(result))]).format( *result )

            sta_num = sta_num + 1
            
            if sta_num % 10000  == 0:
                output_f.flush()
            
        row = f.readline()
    
    for a in obj_file.keys() :
        try:
            obj_file[a].close()
        except IOError:
            continue        

    obj_file = {}
           
    loger.info("total:{0}  statis_num:{1}".format(str(sta_total),str(sta_num)))

def api_init_Statictis(parent, filename, targetpath):
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
            jsonb.update(dict(zip(group_name_api, data_match.groups())))
            verinfo = jsonb['log_9']
            versioninfo_match = p_version.search(verinfo)
            if versioninfo_match:
                jsonb['version'] = versioninfo_match.group(1)
                jsonb['clientinfo'] = versioninfo_match.group(2)
                del jsonb['log_9']
            
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
            
            arg_pid =  jsonb.get('arg_pid','')
            
            if arg_pid and len(arg_pid) == 16:
                filename = arg_pid
            else :
                filename = 'nopid'

            try:
                output_f = obj_file.get(filename, codecs.open(os.path.join(targetpath, filename), 'a', encoding=_encoding, errors=_errors))
            except :
                loger.error('Write File Error. targetpath: %s.  filename: %s. line:%d'  % (filename, filename, sta_total))
                row = f.readline()
                continue
            
            obj_file[filename] = output_f
            result = []
            _args = ['time','ip','url','method','status','version','clientinfo','log_9','arg_sessionid', 'arg_guid', 'arg_vid','arg_type', 'arg_brand', 'arg_btype', 'arg_os', 'arg_wt', 'arg_ht', 'arg_imei', 'arg_imsi', 'arg_deviceid', 'arg_uuid','arg_brand', 'arg_ver', 'arg_time', 'arg_mac', 'arg_operator', 'arg_mobile','arg_uid']
            for _arg in _args:
                result.append(jsonb.get(_arg,'#'))
            
            print >> output_f, u'^_^'.join(['{{{0}}}'.format(i) for i in range(len(result))]).format( *result )
            
            sta_num = sta_num + 1
            
            if sta_num % 10000  == 0:
                output_f.flush()
            
        row = f.readline()
    
    for a in obj_file.keys() :
        try:
            obj_file[a].close()
        except IOError:
            loger.error('IOError! obj_file[%s].close() error.'  % (a))
            continue        

    obj_file = {}
        
    loger.info( "total: {0} statis_num:{1}".format(str(sta_total),str(sta_num)))

def main():
    global loger
    path = sys.argv[2]
    logstr = sys.argv[1]
    posts = logstr.split('.')[1]
    year = logstr[4:8]
    month = logstr[8:10]
    day = logstr[10:12]
    targetpath = sys.argv[3]
    logpath = sys.argv[4]
    if not logpath :
        logpath = '/v5/logs/LogTree/Log/'
    loger = logging.initlog('{0}{1}{2}'.format(os.path.join(logpath), posts, '.log'))
    
    loger.info('Start FileLog.py  {0} {1} {2} {3}'.format(logstr, path, targetpath, logpath))
    
    if  not targetpath :
        targetpath = '/v3/LogTrees'
    for parent, dirnames, filenames  in os.walk(path):    
        for filename in filenames :
            if filename == logstr :
                sta_total =  sta_num = 0
                stime = time.time()
                loger.info( "(*_Statictis) {0} / {1} ? {2}".format(parent, filename, posts))
                if re.search(r'(25|32|33|34)$', parent)  :
                    loger.info( "(api_Statictis) {0} / {1} ? {2}".format(parent, filename, posts))
                    out_dir = os.path.join(targetpath, 'api', year, month, day)
                    if not os.path.exists(out_dir) :
                        os.makedirs(out_dir) 
                    #api_Statictis(parent, filename, out_dir)
                elif re.search(r'(13|26)$', parent) :
                    loger.info( "(wap_Statictis) {0} / {1} ? {2}".format(parent, filename, posts))
                    out_dir = os.path.join(targetpath, 'wap', year, month, day)
                    if not os.path.exists(out_dir) :
                        os.makedirs(out_dir) 
                    wap_Statictis(parent, filename, out_dir)
                elif re.search(r'(16|17)$', parent) :
                    loger.info( "(go_Statictis) {0} / {1} ? {2}".format(parent, filename, posts))
                    out_dir = os.path.join(targetpath, 'go', year, month, day)
                    if not os.path.exists(out_dir) :
                        os.makedirs(out_dir) 
                    #go_Statictis(parent, filename, out_dir)
                elif re.search(r'(12|23)$', parent) :
                    loger.info( "(ios_Statictis) {0} / {1}  ? {2}".format( parent ,filename, posts))
                    out_dir = os.path.join(targetpath, 'ios', year, month, day)
                    if not os.path.exists(out_dir) :
                        os.makedirs(out_dir) 
                    #ios_Statictis(parent, filename, out_dir)
                elif re.search(r'(25-statis|32-statis|33-statis|34-statis)$', parent) :
                    loger.info( "(api_Statictis_statis) {0} / {1}  ? {2}".format( parent ,filename, posts))
                    out_dir = os.path.join(targetpath, 'init-statis', year, month, day)
                    if not os.path.exists(out_dir) :
                        os.makedirs(out_dir) 
                    #api_init_Statictis(parent, filename, out_dir)
                else :
                    continue
                
                etime = time.time()
                loger.info( '*_Statictis({0}, {1}) , Run Time : {2}s'.format(parent, filename, str(etime-stime)))
    
    loger.info('End FileLog.py')
                
if __name__ == '__main__':
    main()
