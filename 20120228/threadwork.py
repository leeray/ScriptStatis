#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Queue, threading, sys
from threading import Thread
import time
import urllib2
import json
import urllib2
import os
import codecs
import re
import redisClient

_encoding = 'utf-8'
_errors='ignore'
workername = '#'
gol_videoinfo = {}
gol_catinfo = {}

# working thread
class Worker(Thread):
    worker_count = 0
    timeout = 1
    def __init__( self, workQueue, resultQueue, **kwds):
        Thread.__init__( self, **kwds )
        self.id = Worker.worker_count
        Worker.worker_count += 1
        self.setDaemon( True )
        self.workQueue = workQueue
        self.resultQueue = resultQueue
        self.start( )

    def run( self ):
        ''' the get-some-work, do-some-work main loop of worker threads '''
        while True:
            try:
                callable, args, kwds = self.workQueue.get(timeout=Worker.timeout)
                res = callable(*args, **kwds)
                #print "worker[%2d]: %s" % (self.id, str(res) )
                #print u'worker{0}: {1}'.format(self.id,  res)
                self.resultQueue.put( res )
                #time.sleep(Worker.sleep)
            except Queue.Empty:
                break
            except :
                print 'worker[%2d]' % self.id, sys.exc_info()[:2]
                raise
                
class WorkerManager:
    def __init__( self, num_of_workers=10, timeout = 2):
        self.workQueue = Queue.Queue()
        self.resultQueue = Queue.Queue()
        self.workers = []
        self.timeout = timeout
        self._recruitThreads( num_of_workers )

    def _recruitThreads( self, num_of_workers ):
        for i in range( num_of_workers ):
            worker = Worker( self.workQueue, self.resultQueue )
            self.workers.append(worker)

    def wait_for_complete( self):
        # ...then, wait for each of them to terminate:
        while len(self.workers):
            worker = self.workers.pop()
            worker.join( )
            if worker.isAlive() and not self.workQueue.empty():
                self.workers.append( worker )
        print "All jobs are are completed."

    def add_job( self, callable, *args, **kwds ):
        self.workQueue.put( (callable, args, kwds) )

    def get_result( self, *args, **kwds ):
        return self.resultQueue.get( *args, **kwds )

def getVideoInfo2(vid):
    global gol_videoinfo
    if gol_videoinfo.get(vid, ''):
        return gol_videoinfo.get(vid)
    cat = ''
    try:
        #path = 'http://api.youku.com/api_ptvideoinfo?pid={0}&id={1}&rt=3'
        path = 'http://10.103.88.96/api_ptvideoinfo?pid=XMTAyOA==&rt=3&id={0}'
        path = path.format(vid)
        content = urllib2.urlopen(path, timeout=200).read()
        videoinfo = json.loads(content)
        result = videoinfo.get('item',{})        
        cats = result.get('cats', '')
        if not cats or len(cats)==0:
            cat = 'NOCAT'
        else:
            cat = cats[0]
    except:
        print 'HTTPError:{0}'.format(vid)
        cat = 'ERRORVID' 
    
    gol_videoinfo[vid] = cat
    return cat

def getVideoInfoFormWeb(vid, vidnum):
    global gol_catinfo
    
    cat = ''
    try:
        cat = redisClient.client().hget('vidtocid',vid)
        if (not cat):
            cat = getVideoInfo2(vid)
    except:
        cat = getVideoInfo2(vid)
    gol_catinfo[cat] = gol_catinfo.get(cat,0) + vidnum

def readLog():
    workername = sys.argv[1]
    targetname = sys.argv[2]
    ac_dict = {}
    for parent, dirnames, filenames  in os.walk('/v5/logs/20120228/SourceLog/'):
        for filename in filenames :
            if workername in filename:
                print filename
                f = codecs.open(os.path.join(parent, filename), 'r', encoding=_encoding, errors=_errors)
                row = f.readline()
                while row.strip():
                    val = row.split(' ')
                    val = [x.strip() for x in val if x]
                    vid = ''
                    if not val[1] or len(val)!=2:
                        row = f.readline()
                        continue
                    else:
                        vid = val[1].strip()
                    
                    ac_dict[vid] = int(val[0])
                   
                    row = f.readline()
    
    import socket
    socket.setdefaulttimeout(10)
    wm = WorkerManager(300)
    for vidkey,vidnum in ac_dict.items():
        wm.add_job( getVideoInfoFormWeb, vidkey, vidnum)
    
    wm.wait_for_complete()
    output_f = codecs.open('/v5/logs/20120228/TargetLog/'+targetname+'.log', 'a', encoding=_encoding, errors=_errors)
    for cat, catnum in gol_catinfo.items():
        print >> output_f, u'{0}:::::{1}'.format(cat, catnum)
    output_f.flush()

if __name__ == '__main__':
    readLog()