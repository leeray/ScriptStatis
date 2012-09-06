#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import sys
import string
import pymongo
import time
import codecs

json_b = {}

_encoding = 'utf-8'
_errors='ignore'

def readfile():
    global client_pid
    f = codecs.open('/home/leeray/workspaces/Python/wanalytics/Statis/otherpy/20120201/guid_upate', 'r', encoding=_encoding, errors=_errors)
    row = f.readline()
    while row:
        _row = row.strip().split(',')
        
        json_b[_row[0]] = _row[1]
        row = f.readline()

def test():
    connection = pymongo.Connection("10.10.116.42", 27017)
    db = connection.stat
    collection = db['clientUser']
    
    a = 1
    
    for guid, lasttime in json_b.items():
        print a
        a += 1
        print 'guid:{0}, lasttime:{1}'.format(guid, lasttime)
        collection.update({'guid':guid}, {'$set':{'lasttime':int(lasttime)}})
        
    
    
#    posts = collection.find()
#    
#    for post in posts:
#        guid = post.get('guid')
#        lasttime = post.get('lasttime')
#        id = post.get('_id')
#        print a
#        a += 1
#        print 'id:{0}, guid:{1}, lasttime:{2}'.format(id, guid, int(lasttime))
#        collection.update({'_id':id}, {'$set':{'lasttime':int(lasttime)}})

def main():    
    time0 = time.time()
    readfile()
    time1 = time.time()
    print 'process time:{0}'.format(time1-time0)
    test()

if __name__ == '__main__':
    main()
 
