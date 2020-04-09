#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import time

path_output = "../output/Topic/"

name_vec = ["字符串",
            "数组", 
            "链表",
            "堆",
            "栈",
            "队列",
            "二叉树",
            "排序算法",
            "查找算法",
            "递归算法",
            "回溯算法",
            "贪心算法",
            "DP算法",
            "DFS算法",
            "BFS算法",
            "二分算法",
            "STL算法",
            "枚举算法",
            "模拟算法",
            "贪心算法",
            "数论",
            "图论",
            "搜索算法",
            "数学",
            "随机化",
            ]


def build_title(s):
    s = s.strip()
    res = "专题-%s" % s
    return res


def build_fname(title):
    res = title + ".md"
    return res


def build_head(title, topic):
    v_year = time.localtime().tm_year
    v_mon = time.localtime().tm_mon
    v_day = time.localtime().tm_mday
    v_hour = time.localtime().tm_hour
    v_min = time.localtime().tm_min
    v_sec = time.localtime().tm_sec

    res = ''
    res += '---\n'
    res += 'title: "%s"\n' % title
    # 标签
    res += 'tags:\n'
    res += '  - leetcode\n'
    res += '  - 专题\n'
    for t in topic:
        s = "  - %s\n" % t
        res += s
    # 分类
    res += 'categories:\n'
    res += '  - leetcode\n'
    res += '  - 专题\n'
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
    res += 'date: %04d-%02d-%02d %02d:%02d:%02d\n' % (v_year, v_mon, v_day, v_hour, v_min, v_sec)
    res += '---\n\n'

    return res



if not os.path.isdir(path_output):
    os.makedirs(path_output)


for i in range(len(name_vec)):
    name = name_vec[i]
    print "%s/%s" % (i, len(name_vec))
    time.sleep(1)
    title = "专题-%s" % name
    topic = [title]
    # 构建文件名称
    fname = build_fname(title)
    fname = os.path.join(path_output, fname)

    # 构建内容，并保存
    with open(fname, "w") as fp:
        # head
        head = build_head(title, topic)
        fp.write(head)

        # 一级标题：题目名称
        fp.write("# " + title + "\n")
        fp.write("\n---\n\n\n")

        # 引言
        fp.write("## 引言\n\n")
        fp.write("\n\n---\n\n\n")

        # 例子
        fp.write("## 例子\n\n")
        # fp.write("\n---\n\n\n")
