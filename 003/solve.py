# solve.py
# coding: UTF-8

from tool import linesplit

def solve(path_to_prbfile):
    groups = []
    prbf = open(path_to_prbfile, 'r')

    line = [line for line in prbf]
    N,M = linesplit(line[0])
    solo = int(N)

    for i in xrange(int(M)):
        rel = linesplit(line[i+1])
        f=0
        #for j in xrange(len(groups)):
        for group in groups:
            first = rel[0] in group
            if first:
                second = rel[1] in group
                # ここでグループの輪をつくってるか確認
                # 鎖だったら追加
                if not(second):
                    group.add(rel[1])
                    solo-=1
                f=1
                break
            second = rel[1] in group
            if second:
                if not(first):
                    group.add(rel[0])
                    solo-=1
                f=1
                break

        if f==0:
            groups.append(set([rel[0],rel[1]]))
            solo-=2

    grouplen = len(groups)

    if grouplen:
        groupintro = grouplen-1
    else:
        groupintro = 0

    return groupintro + solo
