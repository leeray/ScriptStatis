#!/usr/bin/env python
# -*- coding: utf-8 -*-

#找出播放失败的vv，本地播放的vv，和vv总数

import sys

def parse_query(url):
	jsonb = {}
	query = []
	if '?' in url and '='in url:
		query = url.split('?')[1].split('&')
		query = [x.split('=') for x in query]
	query = [('arg_' + y[0], y[1]) for y in query if len(y) == 2]
	jsonb.update(dict(query))
	return jsonb

for line in sys.stdin:
    if 'statis/vv' not in line:
        continue
    
    if 'type=begin' not in line:
        continue
    
    line = line.strip()
    words = line.split(' ')
    if len(words) < 6:
        continue
    urls = words[6] or '/'
    jsonb = parse_query(urls)
    arg_pid = jsonb.get('arg_pid','nopid')
    arg_play_type = jsonb.get('arg_play_type','')
    arg_play_codes = jsonb.get('arg_play_codes', '')
    
    print '%s vv 1' % arg_pid
    
    if arg_play_type and arg_play_types == 'local' :
        print '%s local 1' % arg_pid
    
    if arg_play_codes and arg_play_codes != '200' :
        print '%s playcode 1' % arg_pid
    