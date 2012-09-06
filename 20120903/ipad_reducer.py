#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import sys

_result = {}

for line in sys.stdin:
    line = line.strip()
    _guid, _pv, _vv = line.split(' ')
    
    if not _result[_guid]:
        _result[_guid] = {'pv':0, 'vv':0}
    
    _result[_guid]['pv'] = _result[_guid].get('pv', 0) + _pv
    _result[_guid]['vv'] = _result[_guid].get('vv', 0) + _vv
    
	#print line

for guid, result in _result.item():
    print '%s %s %s' % (guid, result[guid].get('pv'), result[guid].get('vv'))