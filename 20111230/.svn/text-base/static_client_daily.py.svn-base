#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import time
import sys
import codecs
import Logging as logging
import pymongo

_encoding = 'utf-8'
_errors='ignore'

client_pid={}
android2_pid={}

path = sys.argv[1]
date = sys.argv[2]
dir_date = os.path.join(date[:4], date[4:6], date[6:8])
logpath = sys.argv[3]

def file_linecount(file) :  
    count = 0
    for line in open(file).xreadlines(): count += 1
    return count

def read_pid():
    global client_pid
    f = codecs.open('/v5/logs/LogTree/client-pid', 'r', encoding=_encoding, errors=_errors)
    row = f.readline()
    while row:
        _row = row.strip().split('^_^')
        if len(_row) <2 :
            row= f.readline()
            continue
        client_pid[_row[0]] = _row[1]
        row = f.readline()

def read_android2_pid():
    global android2_pid
    f = codecs.open('/v5/logs/LogTree/android2-pid', 'r', encoding=_encoding, errors=_errors)
    row = f.readline()
    while row:
        _row = row.strip().split(',')
        if len(_row) <2 :
            row= f.readline()
            continue
        android2_pid[_row[1]] = _row[0]
        row = f.readline()

def main():
    global loger
    global path
    global date
    global dir_date
    global logpath
    
    loger = logging.initlog('{0}{1}{2}{3}'.format(os.path.join(logpath), 'statis-', date, '.log'))
    loger.info('Start static_client_daily.py  {0} {1} {2}'.format(path, date, logpath))
    stime = time.time()
    read_pid()    
    
    if not path :
        path = '/v3/LogTrees'
    
    connection = pymongo.Connection("10.103.13.42",27017)
    db = connection.DailyLog
    collections = db[date[:6]]

    for parent, dirnames, filenames  in os.walk(path) :
        if dir_date not in parent :
            continue
        for filename in filenames :
            jsonb={}
            jsonb['date'] = date
            jsonb['pid'] = filename
            if filename not in client_pid.keys() :
                loger.info('filename {0}/{1} not in client.'.format(parent, filename))
            else:
                loger.info('filename {0}/{1} in client.'.format(parent, filename))
                jsonb['keyword'] = client_pid[filename]
            
            if 'go' in parent:
                jsonb['server'] = 'go'
            elif 'api' in parent:
                jsonb['server'] = 'api'
            elif 'ios' in parent:
                jsonb['server'] = 'ios'
                jsonb['keyword'] = 'iPhone1'
                jsonb['pid'] = '5e6b1ec70d0bee0c'
            elif 'wap' in parent:
                continue
            else:
                continue
            
            pv = file_linecount(os.path.join(parent, filename))
            jsonb['pv'] = pv
            
            collections.insert(jsonb)
    etime = time.time()
    loger.info('End static_client_daily.py  run time: {0}s'.format(str(etime-stime)))

def initstatis():
    global loger
    global path
    global date
    global dir_date
    global logpath
    
    loger = logging.initlog('{0}{1}{2}{3}'.format(os.path.join(logpath), 'statis-', date, '.log'))
    loger.info('Start init_static_client_daily.py  {0} {1} {2}'.format(path, date, logpath))
    stime = time.time()
    read_android2_pid()
    
    if not path :
        path = '/v3/LogTrees'
    
    connection = pymongo.Connection("10.103.13.42",27017)
    db = connection.DailyLog
    collections = db[date[:6]]

    for parent, dirnames, filenames  in os.walk(path) :
        if dir_date not in parent :
            continue
        for filename in filenames :
           
            jsonb={}
            jsonb['date'] = date
            jsonb['pid'] = filename
            
            if filename not in android2_pid.keys() :
                loger.info('filename {0}/{1} not in Android2.0 Channel List.'.format(parent, filename))
            else:
                loger.info('filename {0}/{1} in Android2.0 Channel List.'.format(parent, filename))
                jsonb['channel'] = android2_pid[filename]
            
            if 'init-statis' in parent:
                jsonb['server'] = 'init-statis'
            else:
                continue
            
            pv = 0
            vv2 = 0
            iphone_vv2 = 0
            iphone_uv1 = 0
            ipad_uv1 = 0
            uv_result1 = []
            uv_result2 = []
            f = codecs.open(os.path.join(parent, filename), 'r', encoding=_encoding, errors=_errors)
            row = f.readline()
            while row:
                pv+=1
                info = row.split('^_^')
                jsonb['server'] = 'api'
                if 'statis/vv' in info[2]:
                    if 'begin' in info[11]:
                        if filename == 'nopid' and 'iPhone' in info[6]:
                            iphone_vv2 += 1
                        else:
                            vv2 += 1
                elif 'initial' in info[2]:
                    uv_result2.append(info[19] + info[24] + info[17] + info[20])
                elif 'getVerInfo' in info[2]:
                    #jsonb['server'] = 'go'
                    if filename == 'nopid' and ('iPhone;' in info[6] or 'iPod' in info[6]):
                        iphone_uv1 += 1
                    elif filename == 'nopid' and 'iPad;' in info[6]:
                        ipad_uv1 += 1
                    else:                 
                        uv_result1.append(info[1])
                else:
                    row = f.readline()
                    continue
                
                row = f.readline()
            
            jsonb['uv1'] = len(set(uv_result1))
            jsonb['uv2'] = len(set(uv_result2))
            jsonb['pv'] = pv
            jsonb['vv2'] = vv2
            jsonb['phone_2_vv'] = iphone_vv2
            
            #print jsonb
            
            upData = collections.find({'date':jsonb['date'], 'pid':jsonb['pid'], 'server':jsonb['server']})
            print 'find {0} row. pid:{1} , date:{2}, uv1:{3}, uv2:{4}, vv2:{5}, phone_2_vv:{6}'.format(upData.count(), jsonb['pid'], jsonb['date'], jsonb['uv1'], jsonb['uv2'], jsonb['vv2'], iphone_vv2)
            #---------------------------------- if filename=='69b81504767483cf':
                # collections.update({'date':jsonb['date'], 'pid':jsonb['pid'], 'server':jsonb['server']}, {'$inc':{'uv1':jsonb['uv1'], 'uv2':jsonb['uv2'], 'statis-pv':jsonb['pv'], 'channel':jsonb.get('channel','')}})
            #------------------------------------------------------------- else:
            collections.update({'date':jsonb['date'], 'pid':jsonb['pid'], 'server':jsonb['server']}, {'$inc':{'vv2':jsonb['vv2'], 'uv1':jsonb['uv1'], 'uv2':jsonb['uv2']} , '$set': { 'statis-pv':jsonb['pv'], 'channel':jsonb.get('channel','')}})
            
            if iphone_vv2 > 0:
                collections.update({'date':jsonb['date'], 'pid':'69b81504767483cf', 'server':'api'}, {'$inc':{'vv2':iphone_vv2}})
            if iphone_uv1 > 0:
                collections.update({'date':jsonb['date'], 'pid':'5e6b1ec70d0bee0c', 'server':'ios'}, {'$inc':{'uv1':iphone_uv1}})
            if ipad_uv1 > 0:
                collections.update({'date':jsonb['date'], 'pid':'a8f2373285115c07', 'server':'api'}, {'$inc':{'uv1':ipad_uv1}})
                
    etime = time.time()
    loger.info('End init_static_client_daily.py  run time: {0}s'.format(str(etime-stime)))

def gouv():
    global loger
    global path
    global date
    global dir_date
    global logpath
   
    loger = logging.initlog('{0}{1}{2}{3}'.format(os.path.join(logpath), 'go-', date, '.log'))
    loger.info('Start static_client_daily.py  {0} {1} {2}'.format(path, date, logpath))
    stime = time.time()
    read_pid() 
    
    if not path :
        path = '/v2/LogTrees'
    
    connection = pymongo.Connection("10.103.13.42",27017)
    db = connection.DailyLog
    collections = db[date[:6]]

    for parent, dirnames, filenames  in os.walk(path) :
        if dir_date not in parent :
            continue
        
        for filename in filenames :
            jsonb={}
            jsonb['date'] = date
            jsonb['pid'] = filename
            
            if 'go' in parent:
                jsonb['server'] = 'go'
            else:
                continue
            
            if filename == 'nopid':
                continue
            
            f = codecs.open(os.path.join(parent, filename) , 'r', encoding=_encoding, errors=_errors)
            row = f.readline()
            result = []
            while row:
                info = row.split('^_^')
                result.append(info[1])
                row = f.readline()
            
            uv1 = len(set(result))
            collections.update({'date':jsonb['date'], 'server':'go', 'pid' : filename}, {'$set':{'uv1':uv1}})

def wapuvvv():
    global loger
    global path
    global date
    global dir_date
    global logpath
    
    loger = logging.initlog('{0}{1}{2}{3}'.format(os.path.join(logpath), 'wap-', date, '.log'))
    loger.info('Start static_client_daily.py  {0} {1} {2}'.format(path, date, logpath))
    stime = time.time()
    read_pid()    
    
    if not path :
        path = '/v2/LogTrees'
    
    connection = pymongo.Connection("10.103.13.42",27017)
    db = connection.DailyLog
    collections = db[date[:6]]

    for parent, dirnames, filenames  in os.walk(path) :
        if dir_date not in parent :
            continue
        
        for filename in filenames :
            jsonb={}
            jsonb['date'] = date
            jsonb['pid'] = filename
            
            if 'wap' in parent:
                jsonb['server'] = 'wap'
                jsonb['keyword'] = 'wap'
            else:
                continue
            
            f = codecs.open(os.path.join(parent, filename) , 'r', encoding=_encoding, errors=_errors)
            result = []
            vv = 0
            pv = 0
            row = f.readline()
            while row:
                pv += 1
                info = row.split('^_^')
                result.append(info[10])
                if '/pvs' in info[2]:
                    vv += 1
                row = f.readline()
            
            jsonb['pv'] = pv
            jsonb['uv1'] = len(set(result))
            jsonb['vv1'] = vv
            
            collections.insert(jsonb)
    etime = time.time()
    loger.info('End static_client_daily.py  run time: {0}s'.format(str(etime-stime)))

def vv1():
    global loger
    global path
    global date
    global dir_date
    global logpath
    
    loger = logging.initlog('{0}{1}{2}{3}'.format(os.path.join(logpath), 'go-', date, '.log'))
    loger.info('Start static_client_daily.py  {0} {1} {2}'.format(path, date, logpath))
    stime = time.time()
    read_pid() 
    
    if not path :
        path = '/v2/LogTrees'
    
    connection = pymongo.Connection("10.103.13.42",27017)
    db = connection.DailyLog
    collections = db[date[:6]]

    for parent, dirnames, filenames  in os.walk(path) :
        if dir_date not in parent :
            continue
        
        for filename in filenames :
            jsonb={}
            jsonb['date'] = date
            jsonb['pid'] = filename
            
            if 'go' in parent:
                jsonb['server'] = 'go'
            elif 'api' in parent:
                jsonb['server'] = 'api'
            elif 'ios' in parent:
                jsonb['server'] = 'ios'
                jsonb['keyword'] = 'iPhone1'
                jsonb['pid'] = '5e6b1ec70d0bee0c'
            elif 'wap' in parent:
                continue
            else:
                continue
            
            f = codecs.open(os.path.join(parent, filename) , 'r', encoding=_encoding, errors=_errors)
            row = f.readline()
            vv1 = 0
            while row:
                info = row.split('^_^')
                vvurl  = '/getVideoDetail'
                if jsonb['server'] == 'ios':
                    vvurl = '/play'
                
                if vvurl in info[2]:
                    vv1 += 1
                
                row = f.readline()
            
            collections.update({'date':jsonb['date'], 'server':jsonb['server'], 'pid' : filename}, {'$inc':{'vv1':vv1}})

if __name__ == '__main__':
    #main()
    #initstatis()
    wapuvvv()
    #gouv()
    #vv1()
    
