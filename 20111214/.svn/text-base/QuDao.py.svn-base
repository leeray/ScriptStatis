#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
import re
import time
import sys
import datetime
import pymongo

qudao_pid = {}

sdate = sys.argv[1]
edate = sys.argv[2]

def read_pid():
    global qudao_pid
    f = codecs.open('./qudaopvuv', 'r', encoding='utf-8')
    row = f.readline()
    while row:
        
        if ',' not in row:
            row = f.readline()
            continue
        row_array = row.split(',')
        
        qudao_pid[row_array[0]] = u'{0}'.format(row_array[1].strip())
        row = f.readline()

def pv():
    global sdate
    global edate    
    pv = ''
    uv = ''
    st_time = datetime.datetime.strptime(sdate, '%Y%m%d')
    ed_time = datetime.datetime.strptime(edate, '%Y%m%d')
    tmp_date = sdate
    day = (ed_time - st_time).days
    connection = pymongo.Connection("10.103.13.42", 27017)
    db = connection.DailyLog
    collection = db[sdate[:6]]
    output_pv = codecs.open('qudao-pv', 'a', encoding='utf-8', errors='ignore')
    output_uv = codecs.open('qudao-uv', 'a', encoding='utf-8', errors='ignore')
    for qudao,pid in qudao_pid.items():
        print qudao
        print pid
        pv=ur'{0},{1}'.format(qudao, pid)
        uv=ur'{0},{1}'.format(qudao, pid)
        
        while (st_time <= ed_time):
            print sdate
            collection = db[sdate[:6]]
            posts = collection.find({'server':'api','pid':pid, 'date':sdate}) 
            st_time = st_time + datetime.timedelta(days=1)
            tmp_pv = 0
            tmp_uv = 0
            for post in posts:
                tmp_pv = post.get('pv', 0)
                tmp_uv = int(post.get('uv1',0)) + int(post.get('uv2',0))
                break
            pv = ur'{0},{1}'.format(pv, tmp_pv)
            uv = ur'{0},{1}'.format(uv, tmp_uv)
            sdate = st_time.strftime('%Y%m%d')
            
        print >> output_pv, u'{0}'.format(pv)
        print >> output_uv, u'{0}'.format(uv)

        st_time = datetime.datetime.strptime(tmp_date, '%Y%m%d')

if __name__ == '__main__':
    read_pid()
    pv()