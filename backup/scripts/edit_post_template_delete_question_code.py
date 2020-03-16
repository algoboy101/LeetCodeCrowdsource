#!/usr/bin/env python
#-*- coding: utf8 -*-
import glob
import os

path_qa = "../../_posts/QA/*.md"

# 读取所有psot
files = glob.glob(path_qa)
files.sort()
# for f in files[:1]:

# 获取所有post的index列表
files_index = []
num = len(files)

for f in files:
# for f in files[:1]:
    with open(f, "r") as fp:
        lines = fp.readlines()
    ind1 = None
    ind2 = None
    for i in range(len(lines)):
        line = lines[i]
        if "## 题目代码" in line:
            ind1 = i
        if "## 题目解析" in line:
            ind2 = i
            break
    if ind1 == None or ind2 == None:
        print(f)
    with open(f, "w") as fp:
        print(num, ind1, ind2)
        for i in range(len(lines)):
            if i >= ind1 and i < ind2:
                continue
            print(lines[i])
            fp.write(lines[i])
