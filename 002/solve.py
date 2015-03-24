# solve.py
# coding: utf-8

from side import find_side

def solve(N,M,noshimochi):

    kirimochi=0
    # [行、行、列、列]
    uplow=[]

    for i in range(N):
        tmp=find_side(noshimochi[i])
        j=i+2
        while N > j:
            spam=find_side(noshimochi[j])
            for k in range(len(spam)):
                if spam[k] in tmp:
                    uplow.append([i, j, spam[k][0], spam[k][1]])
            j+=1

    rotnoshimochi=zip(*noshimochi)
    for i in range(len(uplow)):
        up=uplow[i][2]
        low=uplow[i][3]
        tatesen=[uplow[i][0],uplow[i][1]]
        if (tatesen in find_side(''.join(rotnoshimochi[up]))) and (tatesen in find_side(''.join(rotnoshimochi[low]))):
            kirimochi+=1

    # 発見伝！！
    return kirimochi
