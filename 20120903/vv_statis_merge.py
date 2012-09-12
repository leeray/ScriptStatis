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

result_android_phone = {'vv':0, 'local':0, 'playcode':0, 'PC100':0, 'PC101':0, 'PC102':0, 'PC104':0, 'PC105':0, 'PC106':0, 'PC999':0, 'PCother':0, 'PC200':0, 'PC400':0, 'PC403':0, 'PC0':0, 'PCNULL':0}
result_android_pad = {'vv':0, 'local':0, 'playcode':0, 'PC100':0, 'PC101':0, 'PC102':0, 'PC104':0, 'PC105':0, 'PC106':0, 'PC999':0, 'PCother':0, 'PC200':0, 'PC400':0, 'PC403':0, 'PC0':0, 'PCNULL':0}
result_iphone = {'vv':0, 'local':0, 'playcode':0, 'PC100':0, 'PC101':0, 'PC102':0, 'PC104':0, 'PC105':0, 'PC106':0, 'PC999':0, 'PCother':0, 'PC200':0, 'PC400':0, 'PC403':0, 'PC0':0, 'PCNULL':0}
result_ipad = {'vv':0, 'local':0, 'playcode':0, 'PC100':0, 'PC101':0, 'PC102':0, 'PC104':0, 'PC105':0, 'PC106':0, 'PC999':0, 'PCother':0, 'PC200':0, 'PC400':0, 'PC403':0, 'PC0':0, 'PCNULL':0}

ipad = json.loads(getPid.getPid_json("1")).get("results")
iphone = json.loads(getPid.getPid_json("2")).get("results")
android_phone = json.loads(getPid.getPid_json("4")).get("results")
android_pad = json.loads(getPid.getPid_json("3")).get("results")

vv_file = sys.argv[1]
vv_result_file = sys.argv[2]

f = codecs.open(vv_file, 'r', encoding=_encoding, errors=_errors)
row = f.readline()

while row:
    row = row.strip()
    _pid, _vv, _local, _playcode, _pc200, _pc100, _pc101, _pc102, _pc104, _pc105, _pc106, _pc999, _pc400, _pc403, _pc0, _pcother, _pcnull  = [x.strip() for x in row.split(' ')] 

    
    if _pid in android_phone :
        result_android_phone['vv'] = result_android_phone.get('vv') + int(_vv)
        result_android_phone['local'] = result_android_phone.get('local') + int(_local)
        result_android_phone['playcode'] = result_android_phone.get('playcode') + int(_playcode)
        result_android_phone['PC100'] = result_android_phone.get('PC100') + int(_pc100)
        result_android_phone['PC101'] = result_android_phone.get('PC101') + int(_pc101)
        result_android_phone['PC102'] = result_android_phone.get('PC102') + int(_pc102)
        result_android_phone['PC104'] = result_android_phone.get('PC104') + int(_pc104)
        result_android_phone['PC105'] = result_android_phone.get('PC105') + int(_pc105)
        result_android_phone['PC106'] = result_android_phone.get('PC106') + int(_pc106)
        result_android_phone['PC999'] = result_android_phone.get('PC999') + int(_pc999)
        result_android_phone['PCother'] = result_android_phone.get('PCother') + int(_pcother)
        result_android_phone['PC200'] = result_android_phone.get('PC200') + int(_pc200)
        result_android_phone['PC400'] = result_android_phone.get('PC400') + int(_pc400)
        result_android_phone['PC403'] = result_android_phone.get('PC403') + int(_pc403)
        result_android_phone['PC0'] = result_android_phone.get('PC0') + int(_pc0)
        result_android_phone['PCNULL'] = result_android_phone.get('PCNULL') + int(_pcnull)
    elif _pid in android_pad:
        result_android_pad['vv'] = result_android_pad.get('vv') + int(_vv)
        result_android_pad['local'] = result_android_pad.get('local') + int(_local)
        result_android_pad['playcode'] = result_android_pad.get('playcode') + int(_playcode)
        result_android_pad['PC100'] = result_android_pad.get('PC100') + int(_pc100)
        result_android_pad['PC101'] = result_android_pad.get('PC101') + int(_pc101)
        result_android_pad['PC102'] = result_android_pad.get('PC102') + int(_pc102)
        result_android_pad['PC104'] = result_android_pad.get('PC104') + int(_pc104)
        result_android_pad['PC105'] = result_android_pad.get('PC105') + int(_pc105)
        result_android_pad['PC106'] = result_android_pad.get('PC106') + int(_pc106)
        result_android_pad['PC999'] = result_android_pad.get('PC999') + int(_pc999)
        result_android_pad['PCother'] = result_android_pad.get('PCother') + int(_pcother)
        result_android_pad['PC200'] = result_android_pad.get('PC200') + int(_pc200)
        result_android_pad['PC400'] = result_android_pad.get('PC400') + int(_pc400)
        result_android_pad['PC403'] = result_android_pad.get('PC403') + int(_pc403)
        result_android_pad['PC0'] = result_android_pad.get('PC0') + int(_pc0)
        result_android_pad['PCNULL'] = result_android_pad.get('PCNULL') + int(_pcnull)
    elif _pid in iphone:
        result_iphone['vv'] = result_iphone.get('vv') + int(_vv)
        result_iphone['local'] = result_iphone.get('local') + int(_local)
        result_iphone['playcode'] = result_iphone.get('playcode') + int(_playcode)
        result_iphone['PC100'] = result_iphone.get('PC100') + int(_pc100)
        result_iphone['PC101'] = result_iphone.get('PC101') + int(_pc101)
        result_iphone['PC102'] = result_iphone.get('PC102') + int(_pc102)
        result_iphone['PC104'] = result_iphone.get('PC104') + int(_pc104)
        result_iphone['PC105'] = result_iphone.get('PC105') + int(_pc105)
        result_iphone['PC106'] = result_iphone.get('PC106') + int(_pc106)
        result_iphone['PC999'] = result_iphone.get('PC999') + int(_pc999)
        result_iphone['PCother'] = result_iphone.get('PCother') + int(_pcother)
        result_iphone['PC200'] = result_iphone.get('PC200') + int(_pc200)
        result_iphone['PC400'] = result_iphone.get('PC400') + int(_pc400)
        result_iphone['PC403'] = result_iphone.get('PC403') + int(_pc403)
        result_iphone['PC0'] = result_iphone.get('PC0') + int(_pc0)
        result_iphone['PCNULL'] = result_iphone.get('PCNULL') + int(_pcnull)
    elif _pid in ipad:
        result_ipad['vv'] = result_ipad.get('vv') + int(_vv)
        result_ipad['local'] = result_ipad.get('local') + int(_local)
        result_ipad['playcode'] = result_ipad.get('playcode') + int(_playcode)
        result_ipad['PC100'] = result_ipad.get('PC100') + int(_pc100)
        result_ipad['PC101'] = result_ipad.get('PC101') + int(_pc101)
        result_ipad['PC102'] = result_ipad.get('PC102') + int(_pc102)
        result_ipad['PC104'] = result_ipad.get('PC104') + int(_pc104)
        result_ipad['PC105'] = result_ipad.get('PC105') + int(_pc105)
        result_ipad['PC106'] = result_ipad.get('PC106') + int(_pc106)
        result_ipad['PC999'] = result_ipad.get('PC999') + int(_pc999)
        result_ipad['PCother'] = result_ipad.get('PCother') + int(_pcother)
        result_ipad['PC200'] = result_ipad.get('PC200') + int(_pc200)
        result_ipad['PC400'] = result_ipad.get('PC400') + int(_pc400)
        result_ipad['PC403'] = result_ipad.get('PC403') + int(_pc403)
        result_ipad['PC0'] = result_ipad.get('PC0') + int(_pc0)
        result_ipad['PCNULL'] = result_ipad.get('PCNULL') + int(_pcnull)
    else:
        pass
    
    row = f.readline()

out_f = codecs.open(vv_result_file, 'a', encoding=_encoding, errors=_errors)

print >> out_f, u"OS, VV, 本地VV, 失败VV, 200, -100, -101, -102, -104, -105, -106, -999, 400, 403, 0, other, null"

print >> out_f, "Android Phone, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (result_android_phone['vv'], result_android_phone['local'], result_android_phone['playcode'],result_android_phone['PC200'],result_android_phone['PC100'],result_android_phone['PC101'],result_android_phone['PC102'],result_android_phone['PC104'],result_android_phone['PC105'],result_android_phone['PC106'],result_android_phone['PC999'],result_android_phone['PC400'],result_android_phone['PC403'],result_android_phone['PC0'],result_android_phone['PCother'],result_android_phone['PCNULL'])

print >> out_f, "Android Pad, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (result_android_pad['vv'], result_android_pad['local'], result_android_pad['playcode'],result_android_pad['PC200'],result_android_pad['PC100'],result_android_pad['PC101'],result_android_pad['PC102'],result_android_pad['PC104'],result_android_pad['PC105'],result_android_pad['PC106'],result_android_pad['PC999'],result_android_pad['PC400'],result_android_pad['PC403'],result_android_pad['PC0'],result_android_pad['PCother'],result_android_pad['PCNULL'])

print >> out_f, "iPhone, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (result_iphone['vv'], result_iphone['local'], result_iphone['playcode'],result_iphone['PC200'],result_iphone['PC100'],result_iphone['PC101'],result_iphone['PC102'],result_iphone['PC104'],result_iphone['PC105'],result_iphone['PC106'],result_iphone['PC999'],result_iphone['PC400'],result_iphone['PC403'],result_iphone['PC0'],result_iphone['PCother'],result_iphone['PCNULL'])

print >> out_f, "iPad, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (result_ipad['vv'], result_ipad['local'], result_ipad['playcode'],result_ipad['PC200'],result_ipad['PC100'],result_ipad['PC101'],result_ipad['PC102'],result_ipad['PC104'],result_ipad['PC105'],result_ipad['PC106'],result_ipad['PC999'],result_ipad['PC400'],result_ipad['PC403'],result_ipad['PC0'],result_ipad['PCother'],result_ipad['PCNULL'])


