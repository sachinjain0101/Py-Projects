import threading
import time
import random
import urllib2

#class V:
#    Vx=0

#    @classmethod
#    def increment(cls):
#        return cls.Vx+1

#def sleeper(i):
#    print "\nthread {0} = {1}\n".format(i,V.increment())

#for i in range(1,5):
#    t = threading.Thread(target=sleeper, args=(i,))
#    t.start()

def get_responses():
    urls = ['https://www.google.com', 'https://www.ebay.com', 'https://www.alibaba.com']
    start = time.time()
    for url in urls:
        print url
        resp = urllib2.urlopen(url)
        print resp.getcode()
    print "Elapsed time: %s" % (time.time()-start)

get_responses()
