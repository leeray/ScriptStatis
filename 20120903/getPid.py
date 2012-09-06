#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import sys
import string
import MySQLdb
import connectMySQL
import ConfigParser
#1::ipad
#2::iphone
#3::android pad
#4::android phone
#5::wp7
#6::paike iphone
#7::paike android phone
#8::freewap
#9::channel
#10::factory
#18::内部测试
#21::wap合作

#增加合作模式包含内置渠道和自用的getpid方法
#22:Android-pad包含自用内置和渠道的pid
#23:Android-phone包含自用内置和渠道的pid
#24:Ios-pad包含自用内置和渠道的pid
#25:Ios-phone包含自用内置和渠道的pid
#26:wp7包含自用内置和渠道的pid
#31:Uplayer包含内置和渠道的pid
table_name = "`s_partner_new`"
list = {
'1' : "select `pid` from %s where `os_id` = 52 and `device_type` = 2 and `business_type` = 2 and partner_mode in (1,3,2,8) and `pid_stat` = 1" % table_name, 
'2' : "select `pid` from %s where `os_id` = 52 and `device_type` = 1 and `business_type` = 2 and partner_mode in (1,3,2,8) and `pid_stat` = 1" % table_name, 
'3' : "select `pid` from %s where `os_id` = 61 and `device_type` = 2 and `business_type` = 2 and partner_mode in (1,3,2,8) and `pid_stat` = 1" % table_name, 
'4' : "select `pid` from %s where `os_id` = 61 and `device_type` = 1 and `business_type` = 2 and partner_mode in (1,3,2,8) and `pid_stat` = 1" % table_name, 
'5' : "select `pid` from %s where `os_id` = 59 and `device_type` = 1 and `business_type` = 2 and partner_mode in (1,3,2,8) and `pid_stat` = 1" % table_name, 
'6' : "select `pid` from %s where `os_id` = 52 and `device_type` = 1 and `business_type` = 4 and `pid_stat` = 1" % table_name, 
'7' : "select `pid` from %s where `os_id` = 61 and `device_type` = 1 and `business_type` = 4 and `pid_stat` = 1" % table_name, 
'8' : "select `pid` from %s where `business_type` = 1 and `pid_stat` = 1" % table_name, 
'9' : "select `pid` from %s where `partner_mode` in ('2','8') and `pid_stat` = 1" % table_name, 
'10' : "select `pid` from %s where `partner_mode` = 1 and `pid_stat` = 1" % table_name, 
'18' : "select `pid` from %s where `partner_mode` = 7 and `pid_stat` = 1" % table_name, 
'21' : "select `pid` from %s where `business_type` = 1 and `pid_stat` = 1" % table_name, 
'22' : "select `pid` from %s where `os_id` = 61 and `device_type` = 2 and `business_type` = 2 and `partner_mode` in ('1','2','3','8') and `pid_stat` = 1" % table_name,
'23' : "select `pid` from %s where `os_id` = 61 and `device_type` = 1 and `business_type` = 2 and `partner_mode` in ('1','2','3','8') and `pid_stat` = 1" % table_name,
'24' : "select `pid` from %s where `os_id` = 52 and `device_type` = 2 and `business_type` = 2 and `partner_mode` in ('1','2','3','8') and `pid_stat` = 1" % table_name,
'25' : "select `pid` from %s where `os_id` = 52 and `device_type` = 1 and `business_type` = 2 and `partner_mode` in ('1','2','3','8') and `pid_stat` = 1" % table_name,
'26' : "select `pid` from %s where `os_id` = 59 and `device_type` = 1 and `business_type` = 2 and `partner_mode` in ('1','2','3','8') and `pid_stat` = 1" % table_name,
'31' : "select `pid` from %s where `business_type` = 5 and `partner_mode` = 8 and `device_type` = 1 and `pid_stat` = 1" % table_name,
}

def getPid_json(typeID):
    isInDict = False
    for key in list:
        if 0 == cmp(key, typeID):
            isInDict = True
            break
    if isInDict == False:
        resultStr='{"status": "failed", "typeID": "%s", "code": "4003", "str": "unknown typeID"}' % typeID
        return resultStr
    try:
        db=connectMySQL.connMySQL_mobileProduction()
    except MySQLdb.Error, e:
        print e
        resultStr='{"status": "failed", "typeID": "%s", "code": "4001", "str": "connect database failed"}' % typeID
        return resultStr

    try:
        cursor=db.cursor()
        cursor.execute(list[typeID])
        resultSet=cursor.fetchall()
    except MySQLdb.Error, e:
        print e
        resultStr='{"status": "failed", "typeID": "%s", "code": "4002", "str": "execute SQL failed"}' % typeID
        return resultStr

    valueStr=""
    count=0
    for data in resultSet:
        count+=1
        if (count != len(resultSet)):
            valueStr+='"%s", ' % data
        else:
            valueStr+='"%s"' % data
    resultStr='{"status": "success", "typeID": "%s", "count": "%s", "results": [%s]}' % (typeID, cursor.rowcount, valueStr)
    cursor.close()
    connectMySQL.close(db)
    return resultStr

def getPid_shell(typeID):
    isInDict = False
    for key in list:
        if 0 == cmp(key, typeID):
            isInDict = True
            break
    if isInDict == False:
        resultStr='{"status": "failed", "typeID": "%s", "code": "4003", "str": "unknown typeID"}' % typeID
        return resultStr

    try:
        db=connectMySQL.connMySQL_mobileProduction()
    except MySQLdb.Error, e:
        print e
        resultStr='failed 4001'
        return resultStr

    try:
        cursor=db.cursor()
        cursor.execute(list[typeID])
        resultSet=cursor.fetchall()
    except MySQLdb.Error, e:
        print e
        resultStr='failed 4002'
        return resultStr

    valueStr=""
    count=0
    for data in resultSet:
        count+=1
        if (count != len(resultSet)):
            valueStr+='%s,' % data
        else:
            valueStr+='%s' % data
    resultStr=valueStr
    cursor.close()
    connectMySQL.close(db)
    return resultStr

def getType():
    resultStr='''---------------------------------
typeID\tdesc
1\tipad
2\tiphone
3\tandroid pad
4\tandroid phone
5\twp7
6\tpaike iphone
7\tpaike android phone
8\tfreewap
9\tchannel
10\tfactory
18\t内部测试
21\twap合作
---------------------------------
'''
    return resultStr

def getPaikePid_json():
    try:
        db=connectMySQL.connMySQL_mobileProduction()
    except MySQLdb.Error, e:
        print e
        resultStr='{"status": "failed", "typeID": "paike", "code": "4001", "str": "connect database failed"}'
        return resultStr

    try:
        cursor=db.cursor()
        cursor.execute("select `pid` from %s where `business_type` = 4 and `pid_stat` = 1" % (table_name))
        resultSet=cursor.fetchall()
    except MySQLdb.Error, e:
        print e
        resultStr='{"status": "failed", "typeID": "paike", "code": "4002", "str": "execute SQL failed"}'
        return resultStr

    valueStr=""
    count=0
    for data in resultSet:
        count+=1
        if (count != len(resultSet)):
            valueStr+='"%s", ' % data
        else:
            valueStr+='"%s"' % data
    resultStr='{"status": "success", "typeID": "paike", "count": "%s", "results": [%s]}' % (cursor.rowcount, valueStr)
    cursor.close()
    connectMySQL.close(db)
    return resultStr

# SELECT distinct `s_os`.id, `s_os`.name FROM `s_partner_new`, `s_os` where `s_partner_new`.os_id = `s_os`.id 

def getMainPid_json():
    try:
        db=connectMySQL.connMySQL_mobileProduction()
    except MySQLdb.Error, e:
        print e
        resultStr='{"status": "failed", "typeID": "main", "code": "4001", "str": "connect database failed"}'
        return resultStr

    try:
        cursor=db.cursor()
        cursor.execute("select `pid` from %s where `business_type` = 2 and `os_id` in ('52','59','61') and `partner_mode` = 3 and `device_type` in ('1','2') and pid_stat = 1" % (table_name))
        resultSet=cursor.fetchall()
    except MySQLdb.Error, e:
        print e
        resultStr='{"status": "failed", "typeID": "main", "code": "4002", "str": "execute SQL failed"}'
        return resultStr

    valueStr=""
    count=0
    for data in resultSet:
        count+=1
        if (count != len(resultSet)):
            valueStr+='"%s", ' % data
        else:
            valueStr+='"%s"' % data
    resultStr='{"status": "success", "typeID": "main", "count": "%s", "results": [%s]}' % (cursor.rowcount, valueStr)
    cursor.close()
    connectMySQL.close(db)
    return resultStr

def getChannelPid_json():
    try:
        db=connectMySQL.connMySQL_mobileProduction()
    except MySQLdb.Error, e:
        print e
        resultStr='{"status": "failed", "typeID": "channel", "code": "4001", "str": "connect database failed"}'
        return resultStr

    try:
        cursor=db.cursor()
        cursor.execute("select `pid` from %s where `partner_mode` in ('2','8') and `pid_stat` = 1"% (table_name))
        resultSet=cursor.fetchall()
    except MySQLdb.Error, e:
        print e
        resultStr='{"status": "failed", "typeID": "channel", "code": "4002", "str": "execute SQL failed"}'
        return resultStr

    valueStr=""
    count=0
    for data in resultSet:
        count+=1
        if (count != len(resultSet)):
            valueStr+='"%s", ' % data
        else:
            valueStr+='"%s"' % data
    resultStr='{"status": "success", "typeID": "channel", "count": "%s", "results": [%s]}' % (cursor.rowcount, valueStr)
    cursor.close()
    connectMySQL.close(db)
    return resultStr

def getFactoryPid_json():
    try:
        db=connectMySQL.connMySQL_mobileProduction()
    except MySQLdb.Error, e:
        print e
        resultStr='{"status": "failed", "typeID": "factory", "code": "4001", "str": "connect database failed"}'
        return resultStr

    try:
        cursor=db.cursor()
        cursor.execute("select `pid` from %s where `partner_mode` = 1 and `pid_stat` = 1" % (table_name))
        resultSet=cursor.fetchall()
    except MySQLdb.Error, e:
        print e
        resultStr='{"status": "failed", "typeID": "factory", "code": "4002", "str": "execute SQL failed"}'
        return resultStr

    valueStr=""
    count=0
    for data in resultSet:
        count+=1
        if (count != len(resultSet)):
            valueStr+='"%s", ' % data
        else:
            valueStr+='"%s"' % data
    resultStr='{"status": "success", "typeID": "factory", "count": "%s", "results": [%s]}' % (cursor.rowcount, valueStr)
    cursor.close()
    connectMySQL.close(db)
    return resultStr

def help():
    print '''
[usage]
1. output json format:
  python getPid.py typeID json
2. output shell format:
  python getPid.py typeID shell
[help]
  python getPid.py help
    '''
    print getType()

def isNum(object):
    nums = string.digits
    if type(object) is not str:
        return False
    else:
         for i in object:
             if i not in nums:
                 return False
         return True

def main():
    if len(sys.argv)!=3:
        help()
        exit(1)
    if 0==cmp(sys.argv[2], 'json'):
        if isNum(sys.argv[1])==False:
            pass
            #print getPaikePid_json()
            #print getMainPid_json()
            #print getFactoryPid_json()
            #print getChannelPid_json()
        else:
            print getPid_json(sys.argv[1])
    else:
        if 0==cmp(sys.argv[2], 'shell'):
            print getPid_shell(sys.argv[1])
        else:
            help()
            exit(1)

if __name__ == '__main__':
    main()

