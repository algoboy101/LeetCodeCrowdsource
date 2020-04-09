#!/usr/bin/env python
import glob
import os
import pickle

path_qa = "../../_posts/QA/*.md"

fname_data = "../output/data.pkl"

with open(fname_data, 'rb') as fp:
        # data = pickle.load(fp, encoding='')
        data = pickle.load(fp)

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
        if "https://leetcode.com/" in line:
            index = i
            break
    if index == None:
        print(f)
    else:
        line_url = lines[i]
        # line_url_en = line_url.replace("https://leetcode-cn.com", "https://leetcode.com")
        # line_insert = "* %s\n" % line_url_en
        # lines.insert(index, line_url_en)
        # print(lines[index-1])
        # print(lines[index])
        f_basename = os.path.basename(f)
        ind1 = f_basename.find("[")
        ind2 = f_basename.find("]")
        key = f_basename[ind1+1:ind2]
        line_new_blog = "* %s\n" % data[key]["url_blog"]
        line_new_github = "* [GitHub](%s)\n" % data[key]["url_github"] 
        lines.insert(index, line_new_blog)
        lines.insert(index, line_new_github)
        # print(''.join(lines[index:index+4]))
        # print(data[key]["url_blog"])
        # print(data[key]["url_github"])
        with open(f, "w") as fp:
            for l in lines:
                fp.write(l)
        # print line_url
        # print line_url_en
    