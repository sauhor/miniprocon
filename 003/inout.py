# inout.py
#coding: utf-8

import sys
from solve import solve

argvs=sys.argv
argc=len(argvs)
if argc >= 2:
    res=solve(argvs[1])
else:
    res=solve('prb.txt')

print res
