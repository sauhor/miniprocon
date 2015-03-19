# prime.py
# coding: utf-8

def primeList(num):
    """エラトステネスの篩を使ってn以下の素数リストを返す"""
    if num<1:
        return []
    tmp=range(num+1)
    tmp[0],tmp[1]=False,False
    primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    for i in xrange(len(primes)):
        if num >= primes[i]:
            tmp[primes[i]::primes[i]]=[0]*(num/primes[i])
        else:
            return primes[:i]

    for p in xrange(primes[len(primes)-1],num+1):
        if tmp[p]:
            primes.append(p)
            n=0
            while p+n<len(tmp):
                tmp[p+n]=False
                n+=p
    return primes



def isprime(num,primes=False):
    if not primes:
        primes=primeList(num)
    elif primes[-1]<num:
        primes=primeList(num)
    return num in primes
