#!/usr/bin/env python
#-*- coding: utf8 -*-
import glob
import os

path_qa = "../../_posts/QA/*.md"

# fname_tag = "../source/tags/HOT100.txt"
# fname_tag = "../source/tags/力扣精选算法.txt"
# fname_tag = "../source/tags/精选TOP面试题.txt"
fname_tag = "../source/tags/腾讯精选练习.txt"

def get_index(fname):
    fname_base = os.path.basename(fname)
    ind1 = fname_base.find("[")
    ind2 = fname_base.find("]")
    # print(fname_base, ind1, ind2)
    return fname_base[ind1+1:ind2]

# 获取标签
tag_name = os.path.basename(fname_tag)
tag_name = tag_name.split(".")[0]
print(tag_name)

# 读取所有标签
with open(fname_tag) as fp:
    tags = fp.readlines()
tags = [t.strip() for t in tags]
tags = ["%04d"% int(t) for t in tags]

# 读取所有psot
files = glob.glob(path_qa)
files.sort()
# for f in files[:1]:

# 获取所有post的index列表
files_index = []
for f in files:
    # print(f)
    # print(get_index(f))
    files_index.append(get_index(f))

# 检查tag是否都存在
print("未出现的标签：")
for t in tags:
    # t = "%04d" % int(t)
    if t in files_index:
        pass
    else:
        print(t) 
print("=============")


for f in files:
    fname_index = get_index(f)
    if fname_index in tags:
        # print f
        with open(f, "r") as fp:
            lines = fp.readlines()
        index = None
        for i in range(len(lines)):
            line = lines[i]
            line = line.strip()
            if "categories:" in line:
                index = i
                break
        if index == None:
            print(f)
        else:
            # print(lines[index-1])
            line_new = "  - %s\n" % tag_name
            lines.insert(index, line_new)
            # print(lines[index:index+2])

            with open(f, "w") as fp:
                for l in lines:
                    fp.write(l)
    