#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
import re
import time
import sys
import datetime
import pymongo

sonyericsson_pid = []
se_set = []

sdate = sys.argv[1]
edate = sys.argv[2]

def read_pid():
    global sonyericsson_pid
    global se_set
    f = codecs.open('./SonyEricsson', 'r', encoding='utf-8')
    row = f.readline()
    while row:
        
        if ',' not in row:
            row = f.readline()
            continue
        row_array = row.split(',')

        [(sonyericsson_pid.append(row_array[i].strip())) for i in range(len(row_array)) if len(row_array[i].strip()) == 16]
        
        row = f.readline()
    
    se_set = set(sonyericsson_pid)

def pv():
    print sdate
    print edate
    print se_set
    pv = ''
    uv = ''
    st_time = datetime.datetime.strptime(sdate, '%Y%m%d')
    ed_time = datetime.datetime.strptime(edate, '%Y%m%d')
    day = (ed_time - st_time).days
    connection = pymongo.Connection("10.103.13.42", 27017)
    db = connection.DailyLog
    collection = db[sdate[:6]]
    output_pv = codecs.open('sonyericsson-pv', 'a', encoding='utf-8', errors='ignore')
    output_uv = codecs.open('sonyericsson-uv', 'a', encoding='utf-8', errors='ignore')
    for pid in se_set:
        pv=pid
        uv=pid
        
        while (st_time <= ed_time):
            posts = collection.find({'server':'api','pid':pid, 'date':st_time.strftime('%Y%m%d')}) 
            st_time = st_time + datetime.timedelta(days=1)
            tmp_pv = 0
            tmp_uv = 0
            for post in posts:
                tmp_pv = post.get('pv', 0)
                tmp_uv = int(post.get('uv1',0)) + int(post.get('uv2',0))
                break
            pv = '{0},{1}'.format(pv, tmp_pv)
            uv = '{0},{1}'.format(uv, tmp_uv)
        print >> output_pv, u'{0}'.format(pv)
        print >> output_uv, u'{0}'.format(uv)
        
        st_time = datetime.datetime.strptime(sdate, '%Y%m%d')

if __name__ == '__main__':
    read_pid()
    pv()