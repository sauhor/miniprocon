# solve.py
# coding: utf-8

from prime import primeList
from prime import isprime

def decomp_pnum(num):
    mf=0
    if num<0:
        num*=-1
        mf=1
    primes=primeList(num)
    anscomb=[]
    if isprime(num,primes):
        anscomb.append(num)
    elif isprime(num/2,primes) and (not num%2):
        # 素数の2倍の数のとき（下のループで確認してない）
        anscomb.append(num/2)
        anscomb.append(num/2)
    else:
        if not (num == 1):

            primeNum=len(primes)

            f=1
            i=0
            while i<primeNum and f:
                j=primeNum-1
                while primes[i]<primes[j] and f:
                    if primes[i]+primes[j]==num:
                        anscomb.append(primes[i])
                        anscomb.append(primes[j])
                        f=0
                    elif primes[i]+primes[j]*2==num:
                        anscomb.append(primes[i])
                        anscomb.append(primes[j])
                        anscomb.append(primes[j])
                        f=0
                    elif primes[i]*2+primes[j]==num:
                        anscomb.append(primes[i])
                        anscomb.append(primes[i])
                        anscomb.append(primes[j])
                        #iij
                        f=0
                    j-=1
                i+=1

            if f:
                print "Error"

        else:
            anscomb.append(3)
            anscomb.append(-2)

    if mf:
        anscomb = [x * y for (x, y) in zip(anscomb,[-1]*len(anscomb))]

    return anscomb



def solve(x,y):
    ans=[]
    dpx=decomp_pnum(x)
    dpy=decomp_pnum(y)

    for i in range(len(dpx)):
        if dpx[i]>=0:
            ans.append("R%d" % dpx[i])
        else:
            dpx[i]*=-1
            ans.append("L%d" % dpx[i])

    for i in range(len(dpy)):
        if dpy[i]>=0:
            ans.append("U%d" % dpy[i])
        else:
            dpy[i]*=-1
            ans.append("D%d" % dpy[i])

    return ans
