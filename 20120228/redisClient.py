#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis

pool = redis.ConnectionPool(host='10.103.13.41', port=6379, db=1)

def client():
    r = redis.Redis(connection_pool=pool)
	return r
	