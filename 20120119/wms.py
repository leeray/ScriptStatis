#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import sys
import string
import pymongo


def wms_json(page, pl):
    connection = pymongo.Connection("10.103.13.42", 27017)
    db = connection.wms
    collection = db['feedback']
    
    list = []

    if page and page.isdigit():
        page = int(page)
    else:
        page = 0
    
    if pl and pl.isdigit():
        pl = int(pl)
    else:
        pl = 20
        
    posts = collection.find().skip(page*pl).limit(pl)
    
    for post in posts:
        list.append(post)
    
    return {'list':list}

def main():    
    if len(sys.argv)==2:
        wms_json(sys.argv[1], 20)
    elif len(sys.argv)==3:
        wms_json(sys.argv[1], sys.argv[2])
    else:
        wms_json(0, 20)

if __name__ == '__main__':
    main()
 
