#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import time
import sys
import pymongo
import random
import sys
sys.path.insert(0,'/home/leeray/workspaces/Python/wanalytics/')
from Tools import connectMySQL 
sys.path.insert(0,'/home/leeray/workspaces/Python/wanalytics/Statis/')
from web import _clientCache as clientcache

def main():
    resjson = clientcache.getPromoFactoryName()
    
    if not resjson:
        return
    
    db = connectMySQL.connMySQL_stat()
    c=db.cursor()
    
    arraypid = resjson.get('items',[])
    for i in range(len(arraypid)):
        pidjson = arraypid[i]
        print u'{0}  = {1}'.format(pidjson.get('fid', ''),pidjson.get('name', ''))
        u = 'Youku{0}'.format(str(pidjson.get('fid', '')))
        p = ''.join(random.sample('abcdefghijklmnopquvwxyz1234567890', 6)).replace(" ","")
        c.execute("""INSERT INTO `stat_user`(username, password, fid, type) VALUES(%s, %s, %s, %s) """, (u, p, pidjson.get('fid', ''), 2))
        


if __name__ == '__main__':
    main()
    