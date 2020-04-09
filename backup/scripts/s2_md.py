#!/usr/bin/env python2
#-*- coding:utf8 -*-

"""
通过source/md/*文件获取以下信息：
    # d["answer_desc"]
    # d["topic"]
"""


import glob
import urllib
import os 
import pickle

data = []

fname_src = "../source/src.txt"
fname_data = "../output/data.pkl"
format_md = "../source/md/*.md"
url_img_prefix = "https://raw.githubusercontent.com/algoboy101/LeetCodeCrowdsource/master/imgs/"

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


files_md = glob.glob(format_md)
files_md.sort()

# 遍历所有文件
for fname in files_md:
    # source/md
    index = get_index(fname)
    if index in data:
        flag = True
    else:
        flag = False
    assert flag, "%s not in data" % index
    
    with open(fname, 'r') as fp:
        lines = fp.readlines()
    
    desc = ""
    topic = []

    # 遍历当前文件的所有行
    for line in lines:
        # 处理{{}}
        if "[1096]" in fname:
            line = line.replace("{{", "{\\{")

        # 处理 图片链接
        if "http" in line and  "img" in line:
            url_ind0 = line.find("http")
            url_ind1 = len(line)
            for j in range(url_ind0, len(line)):
                if(line[j] == '"'):
                    url_ind1 = j
                    break
            url = line[url_ind0:url_ind1]
            url_basename = os.path.basename(url)
            url_new = url_img_prefix + url_basename
            line_new = line[:url_ind0] + url_new + line[url_ind1:]
            # print line_new
            # str_url = "![img](%s) \n" % url
            desc = desc + line_new
        else:
            desc = desc + line
        
        # 处理 topic
        if "Related Topics" in line:
            topic = parse_topic(line)
            # print line
            # for t in topic:
            #     print t
            # print topic
        

            
            
    # print desc
    # print "\n\n\n\n"
    data[index]["answer_desc"] = desc
    data[index]["topic"] = topic

    # print data[index]

# 保存文件
with open(fname_data, "wb") as fp:
    pickle.dump(data, fp)

