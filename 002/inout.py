# inout.py
#coding: utf-8

import sys
from solve import solve

argvs=sys.argv
argc=len(argvs)
if argc >= 2:
    f=open(argvs[1],"r")
else:
    f=open("problem.txt","r")
noshi=[line.strip('\n') for line in f]
spam=noshi[0].split(' ')
n=spam[0]
m=spam[1]
noshimochi=noshi[1:]
print solve(int(n),int(m),noshimochi)
