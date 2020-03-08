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

with open(fname_data, 'rb') as fp:
        # data = pickle.load(fp, encoding='')
        data = pickle.load(fp)

for d in data.values():
    flag = ("index" in d) and ("name" in d) and ("title" in d) and ("url_leetcode_cn" in d) and ("url_github" in d) and ("answer_desc" in d) and ("answer_code" in d) and ("topic" in d)
    if not flag:
        print d["index"]
