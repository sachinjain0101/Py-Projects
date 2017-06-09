import threading
import time
import random

def worker(i):
    """thread worker function"""
    print "\nstarting ({0})".format(i)
    r = random.randint(1,15)
    print('\nWorker '+str(i)+' : '+str(r))
    time.sleep(r)
    print "\nending ({0})".format(i)


threads = []
for i in range(5):
    t = threading.Thread(name=str(i),target=worker, args=(i,))
    threads.append(t)
    t.start()