#! /usr/bin/env python
#coding=utf-8

import sys
import urllib

reload(sys)
sys.setdefaultencoding('utf8')

def urldecode(str):
    try:
        query = "query=%s" % str
        d = {}
        a = query.split('&')
        for s in a:
            if s.find('='):
                k,v = map(urllib.unquote, s.split('='))
                try:
                    d[k].append(v)
                except KeyError:
                    d[k] = [v]
        return d["query"][0].decode("utf-8")
    except:
        return ""

def urlencode(str) :
    try:
        reprStr = repr(str).replace(r'\x', '%')
        return reprStr[1:-1]
    except:
        return ""
#也可用urllib.urlencode(m)
#不幸的是，这个函数只能接收key-value pair格式的数据。
#例如：
#m = {'name' : 'peter'; 'gender' : 'male'}
#str = urllib.urlencode(m)
#print str
#gender=male&name=peter

if __name__ == '__main__':
    #str = urlencode("你好")
    #print str
    #print urldecode(str)
    if len(sys.argv)!=3:
        exit(1)
    if 0==cmp(sys.argv[1], '1'):
        print urlencode(sys.argv[2])
    else:
        print urldecode(sys.argv[2])


