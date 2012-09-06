#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import sys
import os

_encoding='utf-8'
_errors='ignore'

reload(sys)
sys.setdefaultencoding('utf-8')

path = sys.argv[1]
iphone_channel_vv = {}
android_channel_vv = {}

for parent, dirnames, filenames  in os.walk(path):
     for filename in filenames :
          
          filedate = filename[24:32]
          
          f = codecs.open(os.path.join(parent, filename), 'r', errors=_errors)
          print '{0}/{1}'.format(parent, filename)
          row = f.readline()
          
          while row:

               channels = unicode(row).strip().split(ur':::::')
               
               if not channels or len(channels)!=2 :
                    row = f.readline()
                    continue
               
               if '69b81504767483cf' in filename:
                    iphone_channel_vv[filedate] = iphone_channel_vv.get(filedate, {})
                    iphone_channel_vv[filedate][channels[0]] = iphone_channel_vv[filedate].get(channels[0],0) + int(channels[1])
               else:
                    android_channel_vv[filedate] = android_channel_vv.get(filedate, {})
                    android_channel_vv[filedate][channels[0]] = android_channel_vv[filedate].get(channels[0],0) + int(channels[1])
         
               row = f.readline()

android_key = []
for key, value in android_channel_vv.items():
     for name, vv in value.items():
          android_key.append(name)

android_key = list(set(android_key))

output_f = codecs.open(os.path.join('/home/lirui/otherpy/20120228/Results', 'android-channel-vv.log'), 'a', encoding=_encoding, errors=_errors)
print >> output_f, 'date'+','.join(android_key)
for key, value in android_channel_vv.items():     
     str = key
     for i in range(len(android_key)):
          str = '{0},{1}'.format(str, value.get(android_key[i], 0))
          
     print >> output_f, u'{0}'.format(str)
output_f.flush()
output_f.close()

print android_channel_vv


iphone_key = []
for key, value in iphone_channel_vv.items():
     for name, vv in value.items():
          iphone_key.append(name)

iphone_key = list(set(iphone_key))

output_f = codecs.open(os.path.join('/home/lirui/otherpy/20120228/Results', 'iphone-channel-vv.log'), 'a', encoding=_encoding, errors=_errors)
print >> output_f, 'date'+','.join(iphone_key)
for key, value in iphone_channel_vv.items():
     str = key
     for i in range(len(iphone_key)):
          str = '{0},{1}'.format(str, value.get(iphone_key[i], 0))
     print >> output_f, u'{0}'.format(str)
output_f.flush()
output_f.close()

print iphone_channel_vv
