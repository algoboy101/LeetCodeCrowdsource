#!/usr/bin/env python
import glob
import os

path_qa = "../../_posts/QA/*.md"

files = glob.glob(path_qa)
files.sort()
# for f in files[:1]:
for f in files:
    # print(f)
    with open(f, "r") as fp:
        lines = fp.readlines()
    index = None
    for i in range(len(lines)):
        line = lines[i]
        line = line.strip()
        if "https://leetcode-cn.com/" in line:
            index = i
            break
    if index == None:
        print(f)
    else:
        line_url = lines[i]
        line_url_en = line_url.replace("https://leetcode-cn.com", "https://leetcode.com")
        # line_insert = "* %s\n" % line_url_en
        lines.insert(index, line_url_en)
        print(lines[index])
        print(lines[index+1])
        with open(f, "w") as fp:
            for l in lines:
                fp.write(l)
        # print line_url
        # print line_url_en
    