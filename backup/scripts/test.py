#!/usr/bin/env python2
# -*- coding:utf8 -*-

import os
import glob

'''
${question.code}
//leetcode submit region begin(Prohibit modification and deletion)
'''

def write_head(title, v_h, v_m, v_s):
    res = ''
    res += '---\n'
    res += 'title: %s\n' % title
    res += 'tags:\n'
    res += '  - leetcode\n'
    res += 'categories:\n'
    res += '  - leetcode\n'
    res += 'author: 张学志\n'
    res += 'comments: true\n'
    res += 'updated: false\n'
    res += 'permalink:\n'
    res += 'mathjax: false\n'
    res += 'top: false\n'
    res += 'description: ...\n'
    res += 'date: 2020-01-01 %02d:%02d:%02d\n' % (v_h, v_m, v_s)
    res += '---\n\n'

    return res


def process_one(fname, fname2, out_path='./output/'):
    if not os.path.isdir(out_path):
        os.makedirs(out_path)
    # fname = '/home/xuezhisd/work/leetcode/[1]Two Sum.cpp'
    # fname = '[608]Tree Node.cpp'
    fname_out = os.path.basename(fname)[:-4] + '.md'
    fname_out = os.path.join(out_path, fname_out)
    # fname_out = fname[:-4] + '.md'
    title = fname[:-4]
    tmp = title.split('[')[-1]
    tmp = tmp.split(']')
    try:
        num = int(tmp[0])
        pre = '[%04d] ' % num
        v_s = num % 60
        v_m = num / 60 % 60
        v_h = num / 3600 % 24
    except:
        pre = '[%s] ' % tmp[0]
        v_s = 60
        v_m = 60
        v_h = 20
    title = '\"' + pre + tmp[1] + '\"'
    # title = '\"[' + title + '\"'
    fname_out = os.path.join(out_path, pre + tmp[1] + '.md')
    # print title
    # print fname_out




    # print num, v_h, v_m, v_s

    # return None

    # print fname
    # print fname_out
    # print title

    # source/cpp
    with open(fname, 'r') as fp:
        lines = fp.readlines()

    ind1 = -1
    ind2 = -1
    ind3 = -1
    ind4 = -1
    flag = True
    for i in range(len(lines)):
        if flag and (not lines[i].startswith("//")):
            ind1 = i
            flag = False
        if lines[i].startswith("${question.code}"):
            ind2 = i
    if ind2 == -1:
        for i in range(len(lines)):
            if lines[i].startswith("//leetcode submit"):
                # print "hello"
                if ind3 == -1:
                    ind3 = i
                else:
                    ind4 = i

    # source/md
    with open(fname2, 'r') as fp:
        lines2 = fp.readlines()


    with open(fname_out, 'w') as fp:

        fp.write(write_head(title, v_h, v_m, v_s))

        fp.write("## 题目描述\n\n")
        # fp.write("```shell\n")
        # for i in range(0, ind1):
        #     fp.write('> ')
        #     line = lines[i]
        #     # if line[2] != ' ':
        #     #     line = line[:2] + ' ' + line[2:]
        #     line = line[2:]
        #     line = line.lstrip()
        #     if line:
        #         fp.write(line)
        #     else:
        #         fp.write('\n')
        # fp.write('```\n')
        for line in lines2:
            if "http" in line and  "img" in line:
                url_ind0 = line.find("http")
                url_ind1 = len(line)
                for j in range(url_ind0, len(line)):
                    if(line[j] == '"'):
                        url_ind1 = j
                        break
                url = line[url_ind0:url_ind1]
                url_basename = os.path.basename(url)
                url_new = "https://raw.githubusercontent.com/algoboy101/note_blog_leetcode/master/imgs/" + url_basename
                line_new = line[:url_ind0] + url_new + line[url_ind1:]
                # str_url = "![img](%s) \n" % url
                fp.write(line_new)
            else:
                fp.write(line)
        fp.write('\n\n')

        fp.write("## 题目代码\n\n")
        fp.write("```cpp\n")
        if ind2 == -1:
            for i in range(ind3+1, ind4):
                fp.write(lines[i])
        else:
            fp.write('\n')
        fp.write('```\n\n')

        fp.write("## 题目解析\n\n")
        fp.write("### 方法一\n\n")
        fp.write("```cpp\n\n")
        fp.write("```\n\n")
        fp.write("### 方法二\n\n")
        fp.write("```cpp\n\n")
        fp.write("```\n\n")
        fp.write("### 方法三\n\n")
        fp.write("```cpp\n\n")
        fp.write("```\n\n")

import urllib
import socket
socket.setdefaulttimeout(10)

if __name__ == '__main__':
    # files = glob.glob("./leetcode2/*.cpp")
    files_cpp = glob.glob("../source/cpp/*.cpp")
    files_md = glob.glob("../source/md/*.md")
    files_cpp.sort()
    files_md.sort()

    assert len(files_cpp) == len(files_md)

    num = len(files_cpp)

    for i in range(num):
        # i = 1000 + i
        print files_cpp[i]
        process_one(files_cpp[i], files_md[i])

    # 下载图片
    # for i in range(num):
    #     fname2 = files_md[i]
    #     with open(fname2, 'r') as fp:
    #         lines2 = fp.readlines()
    #     flag = False
    #     for line in lines2:
    #         if "http" in line and  "img" in line:
    #             flag = True
    #             # print fname2
    #             # print line
    #             url_ind0 = line.find("http")
    #             url_ind1 = len(line)
    #             for j in range(url_ind0, len(line)):
    #                 if(line[j] == '"'):
    #                     url_ind1 = j
    #                     break
    #             url = line[url_ind0:url_ind1]
    #             # print url
    #             # res = ""
    #             # try:
    #             #     res = urllib.urlopen(url).read()
    #             # except:
    #             #     pass
    #             outname = os.path.join("imgs", os.path.basename(url))
    #             if not os.path.isfile(outname):
    #                 print fname2
    #                 print url
    #             # with open(outname, "wb") as fp:
    #             #     fp.write(res)
    #             # print url
