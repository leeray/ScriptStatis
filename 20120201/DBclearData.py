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


def CleariPad(data_date):
    connection = pymongo.Connection("10.103.13.42", 27017)
    db = connection.iPadV2
    collections = db[data_date[:6]]
    collections.remove({'date':data_date})
    
    db2 = connection.iPadV214
    collections2 = db2[data_date[:6]]
    collections2.remove({'date':data_date})
        
def ClearDailyLog(data_date):
    connection = pymongo.Connection("10.103.13.42", 27017)
    db = connection.DailyLog
    collections = db[data_date[:6]]
    collections.remove({'date':data_date})
    
    

def main():
    data_date = sys.argv[1]
    CleariPad(data_date)
    ClearDailyLog(data_date)

if __name__ == '__main__':
    main()
 
