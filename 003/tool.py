# tool.py
# coding: UTF-8

def linesplit(line):
    if line[-1]=='\n':
        return line[0:-1].split(' ')
    else:
        return line.split(' ')
