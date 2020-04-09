#!/usr/bin/env python2
#-*- coding:utf8 -*-

"""
通过source/cpp/*文件获取以下信息：
    # d["answer_code"]
"""


import glob
import urllib
import os 
import pickle

data = []

fname_data = "../output/data.pkl"
format_cpp = "../source/cpp/*.cpp"

"""
解析 索引号
"""
def get_index(s):
    s = s.strip()
    s = ' '.join(s.split())
    s = s.strip()
    s = s.split("]")[0]
    s = s.split("[")[1]
    try:
        index = int(s)
        res = "%04d" % index
    except:
        res = s
    return res


def parse_topic(s):
    res = []
    s = s.strip()
    s = s.split("<li>")
    for item in s:
        if "</li>" in item:
            t = item.split("</li>")[0]
            res.append(t)    
    return res


with open(fname_data, 'rb') as fp:
        # data = pickle.load(fp, encoding='')
        data = pickle.load(fp)

# for d in data:
#     print d

# exit()


files_cpp = glob.glob(format_cpp)
files_cpp.sort()

# 遍历所有文件
for fname in files_cpp:
    # source/cpp
    index = get_index(fname)
    if index in data:
        flag = True
    else:
        flag = False
    assert flag, "%s not in data" % index

    with open(fname, 'r') as fp:
        lines = fp.readlines()
    
    # 计算 标识索引
    ind1 = -1
    ind2 = -1
    ind3 = -1
    ind4 = -1
    flag = True
    for i in range(len(lines)):
        if flag and (not lines[i].startswith("//")):
            ind1 = i
            flag = False
        if lines[i].startswith("${question.code}"):
            ind2 = i
    if ind2 == -1:
        for i in range(len(lines)):
            if lines[i].startswith("//leetcode submit"):
                # print "hello"
                if ind3 == -1:
                    ind3 = i
                else:
                    ind4 = i
    # 扣取代码
    code = ""
    if ind2 == -1:
        for i in range(ind3+1, ind4):
            code = code + lines[i]
    else:
        code = code + "\n"

    data[index]["answer_code"] = code
    # print code
    # print "\n\n\n\n"

# 保存文件
with open(fname_data, "wb") as fp:
    pickle.dump(data, fp)

