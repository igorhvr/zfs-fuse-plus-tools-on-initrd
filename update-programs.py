#!/usr/bin/python
import os
import popen2
from lists import programs

for bin in programs:

    fin, fout = popen2.popen2("/usr/bin/which "+os.path.basename(bin))
    fout.close()
    origin=fin.readline()[:-1]
    if os.path.exists(origin):
        print "getting "+origin+" to source/"+bin
        os.system("cp -u -a -v "+origin+ " source/"+bin)
    else:
        print "could not fetch "+bin+" ("+origin+")"
    
