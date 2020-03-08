#!/usr/bin/env python
# -*- coding:utf8 -*-

# name = "QA"
name_vec = [{"name":"QA", "name_cn":"题解"}, 
            {"name":"Topic", "name_cn":"专题"}]


path_src = "_posts/"
path_dst = "backup/sphinx/source/"


# path_output = 
import glob
import os


def delete_header_of_post(lines):
    indexs = []
    for i in range(len(lines)):
        line = lines[i]
        line = line.strip()
        if line == "---":
            indexs.append(i)
        if len(indexs) == 2:
            break
    if len(indexs) == 2:
        res = lines[indexs[1]+1:]
    else:
        res = lines
    return res


for d in name_vec:
    name = d["name"]
    name_cn = d["name_cn"]
    print(name)
    # 构建路径
    path_src_topic = os.path.join(path_src, name)
    path_dst_topic = os.path.join(path_dst, name)
    format_poster = os.path.join(path_dst_topic, "*.md")
    fname_index = os.path.join(path_dst_topic, "index.rst")

    # 删除 旧文件
    if(os.path.isdir(path_dst_topic) or os.path.isfile(path_dst_topic)):
        os.system("rm %s -rf" % path_dst_topic)
    # 拷贝 新文件
    os.system("cp %s %s -R" % (path_src_topic, path_dst))

    # 获取文件列表，并排序
    files_md = glob.glob(format_poster)
    files_md.sort()

    # 删除md文件的 标签头
    for f in files_md:
        with open(f, 'r') as fp:
            lines = fp.readlines()
        lines = delete_header_of_post(lines)
        content_new = ''.join(lines)
        with open(f, "w") as fp:
            fp.write(content_new)
        
    # 生成QA/index.rst
    with open(fname_index, "w") as fp:
        fp.write("%s\n" % name)
        fp.write("==============\n\n")
        fp.write("..  toctree::\n")
        fp.write("    :maxdepth: 10\n\n")
        for f in files_md:
            fmd = os.path.basename(f)
            fp.write("    " + fmd + "\n") 



exit()