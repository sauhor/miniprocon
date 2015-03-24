# side.py
# coding: UTF-8

def find_lines(line):
    res=[]
    for i in range(len(line)-2):
        j=i+2
        while j < len(line):
            res.append([i,j])
            j+=1
    return res

def find_side(line):

    splitlines=line.split(".")

    res=[]
    p=0
    for i in range(len(splitlines)):

        if len(splitlines[i]) >= 3:
            lines=find_lines(splitlines[i])
            for j in range(len(lines)):
                lines[j][0]+=p
                lines[j][1]+=p
            res+=lines

        if splitlines[i] == 0:
            p+=1
        else:
            p+=len(splitlines[i])+1

    return res
