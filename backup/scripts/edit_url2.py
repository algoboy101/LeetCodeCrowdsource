#!/usr/bin/env python2
#-*- coding:utf8 -*-

import glob
import urllib
import os 

data = []

fname_src = "../source/src.txt"

"""
解析 索引号
"""
def get_index(s):
    s = s.strip()
    s = ' '.join(s.split())
    

    try:
        index = int(s)
        res = "%04d" % index
    except:
        res = s
    return res

"""
解析 名字
"""
def get_name(s):
    item = s.split("]")[0]
    res = item.split("[")[1]
    # res = item[1:]
    res = res.strip()
    res = ' '.join(res.split())
    return res

"""
解析 leetcode_cn 链接
"""
def get_url(s):
    item = s.split(")")[0]
    item = item.split("(")[1]
    res = item.strip()
    return res

"""
通过index和name构建title
"""
def build_title(index, name):
    res = ' '.join([index, name])
    return res

with open(fname_src) as fp:
    lines = fp.readlines()
lines = [line.strip().split('|') for line in lines]


for line in lines:
    d = {}
    index = line[1]
    index = get_index(line[1])
    name = get_name(line[2])
    url_leetcode_cn = get_url(line[2])
    d["index"] = index
    d["name"] = name
    d["title"] = build_title(index, name)
    d["url_leetcode_cn"] = url_leetcode_cn
    data.append(d)
    # d["url_github"]
    # d["url_blog"]
    # d["answer_desc"]
    # d["answer_code"]
    # d["topic"]
    print d

    # s = "%s\t%s\t%s" % (index, name, url_leetcode_cn)
    # print s
    # print line


exit()










prefix = "https://github.com/algoboy101/LeetCodeCrowdsource/blob/master/_posts/QA/"

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
