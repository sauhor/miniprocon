# post.py
# coding: utf-8

import requests
import json
from solve import solve

r=requests.get('http://172.16.108.157/problem')
problem=r.text.split(' ')
x=int(problem[0])
y=int(problem[1])
print x
print y
print "Solving..."
ans=solve(x,y)
ans="\n".join(ans)
print ans
r=requests.post('http://172.16.108.157/post', {'token': 'sauhor','answer': ans})
print r
print r.text
