import time
from threading import Thread
import urllib2

#define a global variable
some_var = 0

class IncrementThread(Thread):
     
    def run(self):
        #we want to read a global variable
        #and then increment it
        global some_var
        read_value = some_var
        print '\nsome_var in %s is %d\n' % (self.name, read_value)
        some_var = read_value + 1 
        print '\nsome_var in %s after increment is %d\n' % (self.name, some_var)

def use_increment_thread():
    threads = []
    rng=10
    for i in range(rng):
        t = IncrementThread()
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print 'After '+rng+' modifications, some_var should have become '+rng
    print 'After '+rng+' modifications, some_var is %d' % (some_var,)

use_increment_thread()