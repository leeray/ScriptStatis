#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 找出ipad的guid, 出现的次数 和 vv的次数

import sys
import re

def parse_query(url):
	jsonb = {}
	query = []
	if '?' in url and '='in url:
		query = url.split('?')[1].split('&')
		query = [x.split('=') for x in query]
	query = [('arg_' + y[0], y[1]) for y in query if len(y) == 2]
	jsonb.update(dict(query))
	return jsonb

ipad_pid = ['87c959fb273378eb', 'a4f46b4582fa09f3', 'a8f2373285115c07']

guid_compile = re.compile(r'^[0-9a-z]{32}$')

for line in sys.stdin:
    
    line = line.strip()
    words = line.split(' ')
    if len(words) < 6:
        continue
    urls = words[6] or '/'
    jsonb = parse_query(urls)
    arg_pid = jsonb.get('arg_pid','nopid')
    arg_guid = jsonb.get('arg_guid', '')
    
    if arg_pid not in ipad_pid:
        continue
    
    if guid_compile.search(arg_guid) :
        if 'statis/vv' in line and 'type=begin' in line:
            print '%s %s %s' % (arg_guid, 1, 1)
        else:
            print '%s %s %s' % (arg_guid, 1, 0)

