#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import time
import sys
import codecs
import Logging as logging
import pymongo
import hashlib
import MySQLdb
import datetime
import url

_encoding = 'utf-8'
_errors='ignore'

_host='10.103.13.14'
_db='statis'
_user='tongji'
_password='123456'

_mongohost='10.103.13.42'
_mongoport=27017

_date = sys.argv[1]
_day = sys.argv[2]
_stimeobj = datetime.datetime.strptime(_date, '%Y%m%d')
_stime = _stimeobj.strftime('%Y-%m-%d 00:00:00')
_etimeobj = _stimeobj + datetime.timedelta(days=int(_day))
_etime = _etimeobj.strftime('%Y-%m-%d 00:00:00')

def mysqltomongodb_api():
    _tmp_list = []
    connection = pymongo.Connection(_mongohost,_mongoport)
    db = connection.ClientUser
    collections = db['User']
    
    dbMysql=MySQLdb.connect(host=_host,db=_db,user=_user,passwd=_password)
    c=dbMysql.cursor()
    
    data = ['guid', 'pid', 'deviceid', 'os', 'btype', 'brand', 'client_ver', 'regtime', 'lasttime', 'operator', 'os_ver']
    sql = "SELECT guid, pid, deviceid, os , btype, brand, ver, ctime, ctime, '', ''  FROM user WHERE server = 'api' and ctime>= '{0}' and ctime < '{1}' ORDER BY id".format(_stime, _etime)
    print sql
    c.execute(sql)  
    posts = c.fetchall()
    s_num = 0
    for x in posts:
        jsonb = {}
        jsonb.update(dict(zip(data, x)))
        
        for key,value in jsonb.items():
            if not value or(isinstance(value, basestring) and value.lower() == "null"):
                jsonb[key] = ''
            
        jsonb['regtime'] = int(time.mktime(jsonb['regtime'].timetuple()))
        jsonb['lasttime'] = int(time.mktime(jsonb['lasttime'].timetuple()))
        jsonb['btype'] = url.urldecode(jsonb['btype'])
        
        _tmp_list.append(jsonb)
        s_num += 1
        if s_num % 10000 == 0:
            print s_num
            collections.insert(_tmp_list)
            _tmp_list = []
        
    if _tmp_list:
        print s_num
        collections.insert(_tmp_list)
        _tmp_list = []

def mysqltomongodb_wap():
    _tmp_list = []
    connection = pymongo.Connection(_mongohost,_mongoport)
    db = connection.WapUser
    collections = db['User']
    
    dbMysql=MySQLdb.connect(host=_host,db=_db,user=_user,passwd=_password)
    c=dbMysql.cursor()
    
    data = ['cookie', 'regtime', 'lasttime']
    sql = "SELECT cookie, ctime, ctime  FROM user WHERE server = 'wap' and ctime>= '{0}' and ctime < '{1}' ORDER BY id".format(_stime, _etime)
    c.execute(sql)  
    posts = c.fetchall()
    s_num = 0
    for x in posts:
        jsonb = {}
        jsonb.update(dict(zip(data, x)))
        jsonb['regtime'] = int(time.mktime(jsonb['regtime'].timetuple()))
        jsonb['lasttime'] = int(time.mktime(jsonb['lasttime'].timetuple()))
        _tmp_list.append(jsonb)
        s_num += 1
        if s_num % 10000 == 0:
            collections.insert(_tmp_list)
            _tmp_list = []
    
    if _tmp_list:
        collections.insert(_tmp_list)
        _tmp_list = []

if __name__ == '__main__':
    mysqltomongodb_api()
    mysqltomongodb_wap()