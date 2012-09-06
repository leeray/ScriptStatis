#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getPid
import sys
import json
import codecs

_encoding = 'utf-8'
_errors='ignore'
android_phone = []
android_pad = []
iphone = []
ipad = []

result_android_phone = {'vv':0, 'local':0, 'playcode':0}
result_android_pad = {'vv':0, 'local':0, 'playcode':0}
result_iphone = {'vv':0, 'local':0, 'playcode':0}
result_ipad = {'vv':0, 'local':0, 'playcode':0}

ipad = json.loads(getPid.getPid_json("1")).get("results")
iphone = json.loads(getPid.getPid_json("2")).get("results")
android_phone = json.loads(getPid.getPid_json("4")).get("results")
android_pad = json.loads(getPid.getPid_json("3")).get("results")

vv_file = sys.argv[1]
vv_result_file = sys.argv[2]

f = codecs.open(vv_file, 'r', encoding=_encoding, errors=_errors)
row = f.readline()

while row:
    line = line.strip()
    _pid, _vv, _local, _playcode = line.split(' ')
    
    if _pid in android_phone :
        result_android_phone['vv'] = result_android_phone.get('vv') + _vv
        result_android_phone['local'] = result_android_phone.get('local') + _local
        result_android_phone['playcode'] = result_android_phone.get('playcode') + _playcode
    elif _pid in android_pad:
        result_android_pad['vv'] = result_android_pad.get('vv') + _vv
        result_android_pad['local'] = result_android_pad.get('local') + _local
        result_android_pad['playcode'] = result_android_pad.get('playcode') + _playcode
    elif _pid in iphone:
        result_iphone['vv'] = result_iphone.get('vv') + _vv
        result_iphone['local'] = result_iphone.get('local') + _local
        result_iphone['playcode'] = result_iphone.get('playcode') + _playcode
    elif _pid in ipad:
        result_ipad['vv'] = result_ipad.get('vv') + _vv
        result_ipad['local'] = result_ipad.get('local') + _local
        result_ipad['playcode'] = result_ipad.get('playcode') + _playcode
    else:
        pass
    
    row = f.readline()

out_f = codecs.open(vv_result_file, 'r', encoding=_encoding, errors=_errors)

print >> out_f, "OS, VV, 本地VV, 失败VV"
print >> out_f, "Android Phone, %s, %s, %s" % (result_android_phone['vv'], result_android_phone['local'], result_android_phone['playcode'])
print >> out_f, "Android Pad, %s, %s, %s" % (result_android_pad['vv'], result_android_pad['local'], result_android_pad['playcode'])
print >> out_f, "iPhone, %s, %s, %s" % (result_iphone['vv'], result_iphone['local'], result_iphone['playcode'])
print >> out_f, "iPad, %s, %s, %s" % (result_ipad['vv'], result_ipad['local'], result_ipad['playcode'])
