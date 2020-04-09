#!/usr/bin/env python2
#-*- coding:utf8 -*-

import glob
import urllib
import os 
prefix = "https://github.com/algoboy101/note_blog_leetcode/blob/master/leetcode/"


files = glob.glob("../../leetcode/*.md")
files.sort()

files = [os.path.basename(f) for f in files]

files_code = [prefix + urllib.quote(f) for f in files]

# print len(files_code)

with open('src.txt') as fp:
    lines = fp.readlines()
lines = [line.strip().split('|') for line in lines]

length = len(lines)

for i in range(length):
    f = files_code[i]
    item = lines[i][2]
    item1 = item.split('http')
    link = 'http' + item1[1]
    link = link.split(')')[0]
    # print link
    tmp = item1[0] + f + ')'
    lines[i][2] = tmp
    print tmp
    # tmp = unicode(tmp)
    # print(tmp)
    # print(type(tmp), tmp)
    # lines[i][2] = item1 + '(' + f + ')'

with open('dst.md', 'w') as fp:   
    for i in range(length):
        tmp = '|'.join(lines[i])
        fp.write(tmp + '\n')
        print tmp


 

# for f in files:
#     print f

# for f in files_code:
#     print f

# s = "[0001] Two Sum.md"

# s_code = urllib.quote(s)

# print prefix + s_code 
