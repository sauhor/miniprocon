# tmp.py
# coding: utf-8

from solve import solve

print "Please input problem"
input_data = input('>>> ')
problem=input_data.split(' ')
x=int(problem[0])
y=int(problem[1])
print "x=%d y=%d" % (x,y)
print "Solving..."
ans=solve(x,y)
print "Answer"
print ans
