#!/usr/bin/python
import os
from lists import programs

for bin in programs:
    print "removing source/"+bin
    if os.path.isfile("source/"+bin): os.remove("source/"+bin)
    