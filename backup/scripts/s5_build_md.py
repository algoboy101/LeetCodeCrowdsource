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
path_output = "../output/QA/"


"""
根据title生成文件名
"""
def build_fname(title):
    res = title + ".md"
    return res


def build_head(title, topic, index):
    try:
        num = int(index)
        v_s = num % 60
        v_m = num / 60 % 60
        v_h = num / 3600 % 24
    except:
        v_s = 60
        v_m = 60
        v_h = 20
    res = ''
    res += '---\n'
    res += 'title: "%s"\n' % title
    # 标签
    res += 'tags:\n'
    res += '  - leetcode\n'
    res += '  - 题解\n'
    for t in topic:
        s = "  - %s\n" % t
        res += s
    # 分类
    res += 'categories:\n'
    res += '  - leetcode\n'
    res += '  - 题解\n'
    # 作者
    res += 'author:\n'
    res += '  - 张学志\n'
    res += '  - 作者2\n'
    res += 'comments: true\n'
    res += 'updated: false\n'
    res += 'permalink:\n'
    res += 'mathjax: true\n'
    res += 'top: false\n'
    res += 'description: ...\n'
    res += 'date: 2020-03-07 %02d:%02d:%02d\n' % (v_h, v_m, v_s)
    res += '---\n\n'

    return res


if not os.path.isdir(path_output):
    os.makedirs(path_output)

with open(fname_data, 'rb') as fp:
        # data = pickle.load(fp, encoding='')
        data = pickle.load(fp)


for d in data.values():
    # 检查是否所有的Key都存在
    flag = ("index" in d) and ("name" in d) and ("title" in d) and ("url_leetcode_cn" in d) and ("url_github" in d) and ("answer_desc" in d) and ("answer_code" in d) and ("topic" in d)
    assert flag, "%s is not OK!" % d["index"]

    # 构建文件名称
    fname = build_fname(d["title"])
    fname = os.path.join(path_output, fname)

    # 构建内容，并保存
    with open(fname, "w") as fp:
        # head
        head = build_head(d["title"], d["topic"], d["index"])
        fp.write(head)
        fp.write("\n")

        # 一级标题：题目名称 + 链接
        fp.write("# " + d["title"] + "\n")
        fp.write("* %s\n" % d["url_leetcode_cn"])
        # fp.write("* %s\n" % d["url_github"])
        # fp.write("\n---\n\n\n")
        fp.write("\n\n")

        # 题目描述
        fp.write("## 题目描述\n\n")
        fp.write(d["answer_desc"])
        # fp.write("\n\n---\n\n\n")
        fp.write("\n\n\n")

        # 题目代码
        fp.write("## 题目代码\n\n")
        fp.write("```cpp\n")
        fp.write(d["answer_code"])
        fp.write('```\n')
        # fp.write("\n---\n\n\n")
        fp.write("\n\n")

        # 题目解析
        fp.write("## 题目解析\n\n\n")
        # for i in ["一", "二", "三", "四"]:
        for i in ["一", "二"]:
            fp.write("### 方法%s\n\n" % i)
            fp.write("#### 分析\n\n")
            fp.write("#### 思路\n\n")
            fp.write("#### 注意\n\n")
            fp.write("#### 知识点\n\n")
            fp.write("#### 复杂度\n\n")
            fp.write("#### 参考\n\n")
            fp.write("#### 答案\n\n")
            fp.write("```cpp\n")
            fp.write("//\n")
            fp.write("```\n")
            fp.write("\n\n")
