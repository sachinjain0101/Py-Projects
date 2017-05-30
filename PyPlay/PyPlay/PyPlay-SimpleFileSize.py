import os
import shutil

print 'START'

outdir = os.getcwd()
    
files=os.listdir(outdir)
print 'Files more than 10KB'
for f in files:
    fwd = os.path.join(outdir,f)
    if int(os.path.getsize(fwd)) > 10000:
        print f

print 'END'

