# inout.py
#coding: utf-8

from solve import solve

f=open("problem.txt","r")
noshi=[line.strip('\n') for line in f]
spam=noshi[0].split(' ')
n=spam[0]
m=spam[1]
noshimochi=noshi[1:]
print solve(int(n),int(m),noshimochi)
