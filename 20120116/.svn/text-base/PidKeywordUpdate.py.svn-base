#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import time
import sys
import pymongo
import codecs

_encoding = 'utf-8'
_errors='ignore'

client_pid={}
android2_pid={}

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
    
    read_pid()
    
    connection = pymongo.Connection("10.103.13.42",27017)
    db = connection.DailyLog
    collections = db['201201']

    posts = collections.find()
    for post in posts:
        pid = post.get('pid','')
        if not pid or pid=='nopid':
            continue
        _id = post['_id']
        keyword = post.get('keyword','')
        date = post['date']
        print '_id:{0}, date:{1}, pid:{2}, keyword:"{3} -> {4}"'.format(_id, date, pid, keyword, client_pid.get(pid,''))
        collections.update({'_id':_id}, {"$set":{'keyword':client_pid.get(pid,'')}})
        


if __name__ == '__main__':
    main()
    