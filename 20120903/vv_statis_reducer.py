#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import sys

_result = {}

for line in sys.stdin:
    line = line.strip()
    _pid, _type, _num = line.split(' ')
    
    if not _result[_pid]:
        _result[_pid] = {'vv':0, 'local':0, 'playcode':0}
    
    if _type = 'local':
        _result[_pid]['local'] = _result[_pid].get('local') + int(_num)
    
    if _type = 'playcode':
        _result[_pid]['playcode'] = _result[_pid].get('playcode') + int(_num)
    
    if _type = 'vv':
        _result[_pid]['vv'] = _result[_pid].get('vv') + int(_num)
    
	#print line

for pid, result in _result.item():
    print '%s %s %s %s' % (pid, result[pid].get('vv'), result[pid].get('local'), result[pid].get('playcode'))