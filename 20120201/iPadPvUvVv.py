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
loger.info('Start iPadPvUvVv.py  {0} {1} {2}'.format(path, date, logpath))

def PvVv():
    
    if not path :
        loger.error('Error: Invalid Path!')
        return
    
    connection = pymongo.Connection("10.103.13.42",27017)
    db = connection.iPadV2
    collections = db[date[:6]]

    for parent, dirnames, filenames  in os.walk(path) :
        if dir_date not in parent :
            continue
        if 'api' not in parent:
            continue
        for filename in filenames :
            if filename != 'a8f2373285115c07':
                continue
            
            jsonb={}
            jsonb['date'] = date
            pv = 0
            vv = 0
            f = codecs.open(os.path.join(parent, filename), 'r', encoding=_encoding, errors=_errors)
            row = f.readline()
            while row:
                info = row.split('^_^')
                if not info[4] or info[4] in ['403' , '404', '500', '502']:
                    row = f.readline()
                    continue
                else:
                    if '/openapi-wireless/getVideoDetail' in info[2]:
                        vv += 1
                    pv += 1
                row = f.readline()
            
            jsonb['pv'] = pv
            jsonb['vv'] = vv
            collections.insert(jsonb)


def Uv():
    ipad_uv = []
    if not path :
        loger.error('Error: Invalid Path!')
        return
    
    connection = pymongo.Connection("10.103.13.42",27017)
    db = connection.iPadV2
    collections = db[date[:6]]
    
    dbMysql=MySQLdb.connect(host=_host,db=_db,user=_user,passwd=_password)
    c=dbMysql.cursor()

    for parent, dirnames, filenames  in os.walk(path) :
        if dir_date not in parent :
            continue
        if 'init-statis' not in parent:
            continue
        for filename in filenames :
            if filename != 'nopid':
                continue
            
            timeobj = datetime.datetime.strptime(date, '%Y%m%d')
            
            jsonb={}
            jsonb['date'] = date
            
            uv = 0
            f = codecs.open(os.path.join(parent, filename), 'r', encoding=_encoding, errors=_errors)
            row = f.readline()
            while row:
                info = row.split('^_^')

                if '/getVerInfo' in info[2]:
                    if not info[4] or info[4] in ['403' , '404', '500', '502']:
                        row = f.readline()
                        continue
                    uid = info[27]
                    if not uid or uid == '#':
                        row = f.readline()
                        continue
                    if 'iPad' not in info[6]:
                        row = f.readline()
                        continue
                    #print 'info[6]:{0}   ######  info[4]:{1}   ######   info[27]:{2}'.format(info[6], info[4],info[27])
                    uv += 1
                    ipad_uv.append(info[27])
                    data = {
                            'uid':info[27],
                            'btype':info[13],
                            'brand':info[12],
                            'ver':info[22],
                            }
                    for key,value in data.items():
                        if value=="#":
                            data[key] = ''
                    
                    _hour = info[0]
                    timeobj1 = timeobj + datetime.timedelta(hours=int(_hour))
                    timestr = timeobj1.strftime('%Y-%m-%d %H:00:00')
                    try:
                        c.execute("""INSERT INTO `ipadv2_user`(uid, ctime, btype, brand, ver) VALUES(%s, %s, %s, %s, %s) """, (data['uid'], timestr, data['btype'], data['brand'], data['ver'] ))
                    except MySQLdb.Error, e:
                        #loger.info("Error %d: %s" % (e.args[0], e.args[1]))
                        pass
                    
                else:
                    row = f.readline()
                    continue
                
                row = f.readline()
    
    uv2 = len(set(ipad_uv))
    
    collections.update({'date':date}, {'$set':{'loginuv':uv, 'uv':uv2}})
    
    stimeobj = datetime.datetime.strptime(date, '%Y%m%d')
    stime = stimeobj.strftime('%Y-%m-%d 00:00:00')
    etimeobj = stimeobj + datetime.timedelta(days=1)
    etime = etimeobj.strftime('%Y-%m-%d 00:00:00')
    sql = "SELECT count(id) FROM ipadv2_user WHERE ctime>= '{0}' and ctime < '{1}'".format(stime, etime)
    c.execute(sql)
    res_count = c.fetchall()
    count = [x[0] for x in res_count]
    if len(count) == 1:
        count = int(count[0])
    collections.update({'date':date}, {'$set':{'new_user':count}})
    #print uv
    #print uv2
    #print count
    #print 'uv:{0} uv:{1} new_user:{2}'.format(uv,uv2,count)

def UpDb():
    connection = pymongo.Connection("10.103.13.42",27017)
    db = connection.iPadV2
    collections = db[date[:6]]
    
    dbMysql=MySQLdb.connect(host=_host,db=_db,user=_user,passwd=_password)
    c=dbMysql.cursor()
    
    stimeobj = datetime.datetime.strptime(date, '%Y%m%d')
    stime = stimeobj.strftime('%Y-%m-%d 00:00:00')
    etimeobj = stimeobj + datetime.timedelta(days=1)
    etime = etimeobj.strftime('%Y-%m-%d 00:00:00')
    sql = "SELECT count(id) FROM ipadv2_user WHERE ctime>= '{0}' and ctime < '{1}'".format(stime, etime)
    print sql
    c.execute(sql)  
    res_count = c.fetchall()
    count = [x[0] for x in res_count]
    if len(count) == 1:
        count = int(count[0])
    print count
    collections.update({'date':date}, {'$set':{'new_user':count}})

if __name__ == '__main__':
    stime = time.time()
    PvVv()
    etime = time.time()
    loger.info('End iPadPvUvVv.py  PvVv() run time: {0}s'.format(str(etime-stime)))
    stime = time.time()
    Uv()
    etime = time.time()
    loger.info('End iPadPvUvVv.py  Uv() run time: {0}s'.format(str(etime-stime)))
    #UpDb()
