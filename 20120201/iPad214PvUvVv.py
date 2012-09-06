#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import time
import sys
import codecs
import Logging as logging
import pymongo
import MySQLdb
import datetime
import hashlib

_encoding = 'utf-8'
_errors='ignore'

_host='10.103.13.14'
_db='statis'
_user='tongji'
_password='123456'

global loger

path = sys.argv[1]
date = sys.argv[2]
dir_date = os.path.join(date[:4], date[4:6], date[6:8])
logpath = sys.argv[3]

loger = logging.initlog('{0}{1}{2}{3}'.format(os.path.join(logpath), 'ipad-', date, '.log'))
loger.info('Start iPad214PvUvVv.py  {0} {1} {2}'.format(path, date, logpath))

def Pv():
    
    if not path :
        loger.error('Error: Invalid Path!')
        return
    
    connection = pymongo.Connection("10.103.13.42",27017)
    db = connection.iPadV214
    collections = db[date[:6]]

    for parent, dirnames, filenames  in os.walk(path) :
        if dir_date not in parent :
            continue
        if 'api' not in parent:
            continue
        for filename in filenames :
            if filename != '87c959fb273378eb':
                continue
            
            jsonb={}
            jsonb['date'] = date
            pv = 0
            f = codecs.open(os.path.join(parent, filename), 'r', encoding=_encoding, errors=_errors)
            row = f.readline()
            while row:
                info = row.split('^_^')
                if not info[4] or info[4] in ['403' , '404', '500', '502']:
                    row = f.readline()
                    continue
                else:
                    pv += 1
                row = f.readline()
            
            jsonb['pv'] = pv
            collections.insert(jsonb)

def UvVv():

    if not path :
        loger.error('Error: Invalid Path!')
        return
    
    vv = 0
    uv = 0
    ipad_uv = []
    
    connection = pymongo.Connection("10.103.13.42",27017)
    db = connection.iPadV214
    collections = db[date[:6]]
    
    dbMysql=MySQLdb.connect(host=_host,db=_db,user=_user,passwd=_password)
    c=dbMysql.cursor()
    
    for parent, dirnames, filenames  in os.walk(path) :
        if dir_date not in parent :
            continue
        if 'init-statis' not in parent:
            continue
        for filename in filenames :
            if filename != '87c959fb273378eb':
                continue
            
            timeobj = datetime.datetime.strptime(date, '%Y%m%d')
            
            jsonb={}
            jsonb['date'] = date
            
            vv = 0
            uv = 0
            f = codecs.open(os.path.join(parent, filename), 'r', encoding=_encoding, errors=_errors)
            row = f.readline()
            while row:
                info = row.split('^_^')

                if '/initial' in info[2]:
                    if not info[4] or info[4] in ['403' , '404', '500', '502']:
                        row = f.readline()
                        continue
                    data = {
                            'mac':info[24],
                            'imei':info[17],
                            'deviceid':info[19],
                            'uuid':info[20],
                            'pid':filename,
                            'os':info[14],
                            'btype':info[13],
                            'brand':info[12],
                            'ver':info[22],
                            }
                    for key,value in data.items():
                        if value=="#":
                            data[key] = ''
                    
                    uv += 1
                    guid = '{mac}&{imei}&{deviceid}&{uuid}'.format(**data)
                    guid = hashlib.md5(guid).hexdigest()
                    ipad_uv.append(guid)
                    
                    _hour = info[0]
                    timeobj1 = timeobj + datetime.timedelta(hours=int(_hour))
                    timestr = timeobj1.strftime('%Y-%m-%d %H:00:00')
                    try:
                        c.execute("""INSERT INTO `ipadv214_user`(guid, ctime, btype, brand, ver) VALUES(%s, %s, %s, %s, %s) """, (guid, timestr, data['btype'], data['brand'], data['ver'] ))
                    except MySQLdb.Error, e:
                        #loger.info("Error %d: %s" % (e.args[0], e.args[1]))
                        pass
                elif '/statis/vv' in info[2]:
                    if 'begin' in info[11]:
                        vv += 1 
                else:
                    row = f.readline()
                    continue
                
                row = f.readline()
    
    uv2 = len(set(ipad_uv))
    
    collections.update({'date':date}, {'$set':{'loginuv':uv, 'uv':uv2, 'vv': vv}})
    
    stimeobj = datetime.datetime.strptime(date, '%Y%m%d')
    stime = stimeobj.strftime('%Y-%m-%d 00:00:00')
    etimeobj = stimeobj + datetime.timedelta(days=1)
    etime = etimeobj.strftime('%Y-%m-%d 00:00:00')
    sql = "SELECT count(id) FROM ipadv214_user WHERE ctime>= '{0}' and ctime < '{1}'".format(stime, etime)
    c.execute(sql)
    res_count = c.fetchall()
    count = [x[0] for x in res_count]
    if len(count) == 1:
        count = int(count[0])
    collections.update({'date':date}, {'$set':{'new_user':count}})

if __name__ == '__main__':
    stime = time.time()
    Pv()
    etime = time.time()
    loger.info('End iPad214PvUvVv.py  Pv() run time: {0}s'.format(str(etime-stime)))
    stime = time.time()
    UvVv()
    etime = time.time()
    loger.info('End iPad214PvUvVv.py  UvVv() run time: {0}s'.format(str(etime-stime)))
