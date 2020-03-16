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

'''
修改 ### 方法一 -> ### 方法一：算法名称
'''

# for f in files:
# # for f in files[:1]:
#     with open(f, "r") as fp:
#         lines = fp.readlines()
#     inds = []
#     for i in range(len(lines)):
#         line = lines[i]
#         if "### 方法" in line:
#             inds.append(i)
            
#     if len(inds) == 0:
#         print(f)
#     for j in inds:
#         line = lines[j].strip()
#         line = "%s：[算法名称]\n" % line
#         lines[j] = line
#         print line
    
#     with open(f, "w") as fp:
#         for i in range(len(lines)):
#             fp.write(lines[i])




'''
删除 #### 参考
'''

# for f in files:
# # for f in files[:1]:
#     with open(f, "r") as fp:
#         lines = fp.readlines()
#     inds = []
#     for i in range(len(lines)):
#         line = lines[i]
#         if "#### 参考" in line:
#             inds.append(i)
            
#     if len(inds) == 0:
#         print(f)
#     print(inds)

#     for j in inds:
#         # line = lines[j].strip()
#         # line = "%s：[算法名称]\n" % line
#         lines[j] = ""
#         lines[j+1] = ""
#         # print line
    
#     with open(f, "w") as fp:
#         for i in range(len(lines)):
#             fp.write(lines[i])




'''
修改 #### 答案 -> 代码
'''

# for f in files:
# # for f in files[:1]:
#     with open(f, "r") as fp:
#         lines = fp.readlines()
#     inds = []
#     for i in range(len(lines)):
#         line = lines[i]
#         if "#### 答案" in line:
#             inds.append(i)
            
#     if len(inds) == 0:
#         print(f)
#     for j in inds:
#         lines[j] = "#### 代码\n"
#         # print line
    
#     with open(f, "w") as fp:
#         for i in range(len(lines)):
#             fp.write(lines[i])


'''
添加 ## 相关题目
'''

for f in files:
# for f in files[:1]:
    with open(f, "r") as fp:
        lines = fp.readlines()
    
    with open(f, "w") as fp:
        for i in range(len(lines)):
            fp.write(lines[i])
        fp.write("## 相关题目\n")
        fp.write("* \n")
