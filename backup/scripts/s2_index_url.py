#!/usr/bin/env python2
#-*- coding:utf8 -*-

"""
检查是否所有的Key都存在
"""

import glob
import urllib
import os
import pickle

# data = {}

fname_data = "../output/data.pkl"
fname_index_url = "../source/index_url.txt"

with open(fname_data, 'rb') as fp:
        # data = pickle.load(fp, encoding='')
        data = pickle.load(fp)

with open(fname_index_url, "r") as fp:
    index_url = fp.readlines()
index_url = [l.strip() for l in index_url]

index_url_dict = {}
for i in range(len(index_url)):
    l = index_url[i]
    ind = l.find("http")
    k = l[:ind].strip()
    v = l[ind:]
    index_url_dict[k] = v
    # print(k, v)

# index_url_dict = {}
# for l in index_url:
#     print l
#     index_url_dict[l[0]] = l[1]

for key in data.keys():
    if key not in index_url_dict:
        print key
    data[key]["url_blog"] = index_url_dict[key]
    if(len(data[key]["url_blog"])) < 20:
        print data[key]

# 创建文件夹
if not os.path.isdir(os.path.dirname(fname_data)):
    os.makedirs(os.path.dirname(fname_data))

# 保存文件
with open(fname_data, "wb") as fp:
    pickle.dump(data, fp)