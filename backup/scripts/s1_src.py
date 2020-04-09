#!/usr/bin/env python2
#-*- coding:utf8 -*-

"""
通过source/src.txt文件获取以下信息：
    d["index"] = index
    d["name"] = name
    d["title"] = build_title(index, name)
    d["url_leetcode_cn"] = url_leetcode_cn
    d["url_leetcode"]
"""


import glob
import urllib
import os 
import pickle
import urllib

data = {}

fname_src = "../source/src.txt"
fname_data = "../output/data.pkl"
# url_github_prefix = "https://raw.githubusercontent.com/algoboy101/LeetCodeCrowdsource/master/_posts/QA/"
url_github_prefix = "https://github.com/algoboy101/LeetCodeCrowdsource/tree/master/_posts/QA/"

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
    ind = s.find("https")
    s = s[ind:]
    res = s.split(")")[0]
    # item = item.split("(")[1]
    # res = item.strip()
    return res

"""
解析 leetcode_en 链接
"""
def get_url_en(url_cn):
    url_en = url_cn.replace("https://leetcode-cn.com", "https://leetcode.com")
    return url_en

"""
通过index和name构建title
"""
def build_title(index, name):
    res = "[%s] %s" % (index, name)
    # res = ' '.join([index, name])
    return res

"""
根据title生成文件名
"""
def build_fname(title):
    res = title + ".md"
    return res

with open(fname_src) as fp:
    lines = fp.readlines()
lines = [line.strip().split('|') for line in lines]


for line in lines:
    d = {}
    index = line[1]
    index = get_index(line[1])
    name = get_name(line[2])
    title = build_title(index, name)
    url_leetcode_cn = get_url(line[2])
    url_leetcode_en = get_url_en(url_leetcode_cn)
    fname = build_fname(title)
    url_github = url_github_prefix + urllib.quote(fname)
    d["index"] = index
    d["name"] = name
    d["title"] = title
    d["url_leetcode_cn"] = url_leetcode_cn
    d["url_leetcode_en"] = url_leetcode_en
    d["url_github"] = url_github

    data[index] = d
    # data.append(d)
    # d["url_blog"]
    # d["answer_desc"]
    # d["answer_code"]
    # d["topic"]
    # print d
    
    # s = "%s\t%s\t%s" % (index, name, url_leetcode_cn)
    # print s
    # print line

# data.sort()
# for d in data:
#     print d

# 创建文件夹
if not os.path.isdir(os.path.dirname(fname_data)):
    os.makedirs(os.path.dirname(fname_data))

# 保存文件
with open(fname_data, "wb") as fp:
    pickle.dump(data, fp)
