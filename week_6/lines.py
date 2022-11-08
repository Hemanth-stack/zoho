import sys
import os


if len(sys.argv) == 2:
    file = open(os.path.join('/home/local/ZOHOCORP/hemanth-pt6518/Desktop/vs',sys.argv[1]),'r')
    length = len(file.readlines())
    blank_space = 0
    comments = 0
    file.seek(0)
    for i in file.readlines():
        print(len(i))
        if len(i) == 1: 
            blank_space += 1
        if '#' in i:
            comments += 1 
    print(length - blank_space)
else:
    sys.exit()