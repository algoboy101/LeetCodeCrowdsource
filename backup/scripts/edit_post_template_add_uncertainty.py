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
    ind2 = None
    for i in range(len(lines)):
        line = lines[i]
        if "## 题目解析" in line:
            ind2 = i
            break
    if ind2 == None:
        print(f)
    with open(f, "w") as fp:
        for i in range(len(lines)):
            # print(lines[i])
            fp.write(lines[i])
            if i == ind2:
                fp.write("* [请一句话描述题目...]\n\n")
                fp.write("### 不确定性\n")
