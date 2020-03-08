#!/usr/bin/env python2
# -*- coding:utf8 -*-

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



import os 
def process_one(fname, out_path='./output/'):
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

    with open(fname_out, 'w') as fp:
        
        fp.write(write_head(title, v_h, v_m, v_s))

        fp.write("## 题目描述\n\n")
        # fp.write("```shell\n")
        for i in range(0, ind1):
            fp.write('> ')
            line = lines[i]
            # if line[2] != ' ':
            #     line = line[:2] + ' ' + line[2:]
            line = line[2:]
            line = line.lstrip()
            if line:
                fp.write(line)
            else:
                fp.write('\n')
        # fp.write('```\n')
        fp.write('\n')

        fp.write("## 题目代码\n\n")
        fp.write("```cpp\n")
        if ind2 == -1:
            for i in range(ind3+1, ind4):
                fp.write(lines[i])
        else:
            fp.write('\n')
        fp.write('```\n\n')

        fp.write("## 解析\n\n")
        fp.write("### 方法一\n\n")
        fp.write("```cpp\n\n")
        fp.write("```\n\n")
        fp.write("### 方法二\n\n")
        fp.write("```cpp\n\n")
        fp.write("```\n\n")
        fp.write("### 方法三\n\n")
        fp.write("```cpp\n\n")
        fp.write("```\n\n")


import glob
if __name__ == '__main__':
    # files = glob.glob("./leetcode2/*.cpp")
    files = glob.glob("./leetcode/*.cpp")
    for file in files:
        print file
        process_one(file)
    