#!/usr/bin/env python
#-*- coding:utf8 -*-
import glob
import os
import pickle
import collections

fname_data = "../output/data.pkl"
fname_output = "../output/table_url.md"

with open(fname_data, 'rb') as fp:
        # data = pickle.load(fp, encoding='')
        data = pickle.load(fp)

# data_sort = collections.OrderedDict()
data_sort = collections.OrderedDict(sorted(data.items(), key=lambda t: t[0]))

# for k, v in data.items():
#     data_sort[k] = v
    

# with open(fname_output, 'w') as fp:
#     fp.write("| 索引 | 题目 | Blog | Github | LeetCode | LeetCode-cn |\n")
#     fp.write("|---|---|---|---|---|---|\n")
#     for k, v in data_sort.items():
#         # print k
#         # continue
#         d = v
#         col1_index = d["index"]
#         col2_name = d["name"]
#         col3_blog = d["url_blog"]
#         col4_github = d["url_github"]
#         col5_leetcode_en = d["url_leetcode_en"]
#         col6_leetcode_cn = d["url_leetcode_cn"]  
#         line = "| %s | %s | [Blog](%s) | [Github](%s) | [LeetCode](%s) | [LeetCode-cn](%s) |\n" % (col1_index, col2_name, col3_blog, col4_github, col5_leetcode_en, col6_leetcode_cn)
#         print line
#         fp.write(line)

with open(fname_output, 'w') as fp:
    fp.write("| 索引 | 题目 | Blog | Github | LeetCode |\n")
    fp.write("|---|---|---|---|---|\n")
    for k, v in data_sort.items():
        # print k
        # continue
        d = v
        col1_index = d["index"]
        col2_name = d["name"]
        col3_blog = d["url_blog"]
        col4_github = d["url_github"]
        col5_leetcode_en = d["url_leetcode_en"]
        col6_leetcode_cn = d["url_leetcode_cn"]  
        line = "| %s | %s | [Blog](%s) | [Github](%s) | [LeetCode](%s) |\n" % (col1_index, col2_name, col3_blog, col4_github, col6_leetcode_cn)
        print line
        fp.write(line)

# with open(fname_output, 'w') as fp:
#     fp.write("| 索引 | 题目 | Blog | LeetCode | LeetCode-cn |\n")
#     fp.write("|---|---|---|---|---|\n")
#     for k, v in data_sort.items():
#         # print k
#         # continue
#         d = v
#         col1_index = d["index"]
#         col2_name = d["name"]
#         col3_blog = d["url_blog"]
#         col4_github = d["url_github"]
#         col5_leetcode_en = d["url_leetcode_en"]
#         col6_leetcode_cn = d["url_leetcode_cn"]  
#         line = "| %s | [%s](%s) | [Blog](%s) | [LeetCode](%s) | [LeetCode-cn](%s) |\n" % (col1_index, col2_name, col4_github, col3_blog, col5_leetcode_en, col6_leetcode_cn)
#         print line
#         fp.write(line)


# with open(fname_output, 'w') as fp:
#     fp.write("| 索引 | 题目 | 申请人 |\n")
#     fp.write("|---|---|---|\n")
#     for k, v in data_sort.items():
#         # print k
#         # continue
#         d = v
#         col1_index = d["index"]
#         col2_name = d["name"]
#         col3_blog = d["url_blog"]
#         col4_github = d["url_github"]
#         col5_leetcode_en = d["url_leetcode_en"]
#         col6_leetcode_cn = d["url_leetcode_cn"]  
#         line = "| %s | [%s](%s) |  |\n" % (col1_index, col2_name, col3_blog)
#         print line
#         fp.write(line)