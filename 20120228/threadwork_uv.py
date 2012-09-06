#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Queue, threading, sys
from threading import Thread
import time
import urllib2
import json
import os
import codecs
import re

_encoding = 'utf-8'
_errors = 'ignore'
workername = '#'
gol_videoinfo = {}
gol_catinfo = {}

# working thread
class Worker(Thread):
    worker_count = 0
    timeout = 1
    def __init__(self, workQueue, resultQueue, catInfo, **kwds):
        Thread.__init__(self, **kwds)
        self.id = Worker.worker_count
        Worker.worker_count += 1
        self.setDaemon(True)
        self.workQueue = workQueue
        self.resultQueue = resultQueue
        self.catInfo = catInfo
        self.start()

    def run(self):
        while True:
            try:
                callable, args, kwds = self.workQueue.get(timeout=Worker.timeout)
                res = callable(self.catInfo, *args, **kwds)
                #print "worker[%2d]: %s" % (self.id, str(res) )
                #print u'worker{0}: {1}'.format(self.id,  res)
                self.resultQueue.put(res)
                #time.sleep(Worker.sleep)
            except Queue.Empty:
                break
            except :
                print 'worker[%2d]' % self.id, sys.exc_info()[:2]
                raise
                
class WorkerManager:
    def __init__(self, num_of_workers=10, timeout=2):
        self.workQueue = Queue.Queue()
        self.resultQueue = Queue.Queue()
        self.workers = []
        self.timeout = timeout
        self.catInfo = []
        self._recruitThreads(num_of_workers)

    def _recruitThreads(self, num_of_workers):
        for i in range(num_of_workers):
            self.catInfo.append({})
            worker = Worker(self.workQueue, self.resultQueue, self.catInfo[i])
            self.workers.append(worker)

    def wait_for_complete(self):
        while len(self.workers):
            worker = self.workers.pop()
            worker.join()
            if worker.isAlive() and not self.workQueue.empty():
                self.workers.append(worker)
        print "All jobs are are completed."
        for i in range(len(self.catInfo)):
            tmpcatinfo = self.catInfo[i]
	    #print tmpcatinfo
	    for key,value in tmpcatinfo.items():
                gol_catinfo[key] = gol_catinfo.get(key, [])
		gol_catinfo[key].extend(value)

    def add_job(self, callable, *args, **kwds):
        self.workQueue.put((callable, args, kwds))

    def get_result(self, *args, **kwds):
        return self.resultQueue.get(*args, **kwds)

def getVideoInfo2(vid):
    cat = ''
    try:
        path = 'http://10.103.88.96/api_ptvideoinfo?pid=XMTAyOA==&rt=3&id={0}'
        path = path.format(vid)
        content = urllib2.urlopen(path, timeout=200).read()
        videoinfo = json.loads(content)
        result = videoinfo.get('item', {})        
        cats = result.get('cats', '')
        if not cats or len(cats) == 0:
            cat = 'NOCAT'
        else:
    	    if not cats[0]:
    	        cat = 'NOCAT'
    	    else:
    	    	cat = cats[0]
    except:
        print 'HTTPError:{0}'.format(vid)
        cat = 'ERRORVID' 
    
    return cat

def getVideoInfoFormWeb(catInfo, vid, guid):
    cat = getVideoInfo2(vid)
    catInfo[cat] = catInfo.get(cat, [])
    catInfo[cat].append(guid)

def readLog():
    workername = sys.argv[1]
    targetname = sys.argv[2]
    ac_dict = {}
    for parent, dirnames, filenames  in os.walk('/home/lirui/otherpy/20120228/UVSourceLog/'):
        for filename in filenames :
            if workername in filename:
                print filename
                f = codecs.open(os.path.join(parent, filename), 'r', encoding=_encoding, errors=_errors)
                row = f.readline()
                while row.strip():
                    val = row.split(' ')
                    val = [x.strip() for x in val if x]
                    vid = ''
                    if not val[1] or len(val) != 3:
                        row = f.readline()
                        continue
                    else:
                        vid = val[1].strip()
                    
                    ac_dict[vid] = val[2]
		    
                    row = f.readline()

    import socket
    socket.setdefaulttimeout(10)
    wm = WorkerManager(300)
    for vidkey, guid in ac_dict.items():
        wm.add_job(getVideoInfoFormWeb, vidkey, guid)

    wm.wait_for_complete()

    output_f = codecs.open('/home/lirui/otherpy/20120228/UVTargetLog/' + targetname + '.log', 'a', encoding=_encoding, errors=_errors)
    for cat, guids in gol_catinfo.items():
        print >> output_f, u'{0}:::::{1}'.format(cat, len(set(guids)))
    output_f.flush()

if __name__ == '__main__':
    readLog()
