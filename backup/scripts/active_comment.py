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
    
urls = []

for k, v in data_sort.items():
        # print k
        # continue
        d = v
        col3_blog = d["url_blog"]
        urls.append(col3_blog)
import time
t = 0
# for url in urls[300:350]:
# for url in urls[700:750]:
# for url in urls[750:800]:
# for url in urls[800:850]:
# for url in urls[850:900]:
# for url in urls[900:950]:
# for url in urls[950:1000]:
# for url in urls[1000:1050]:
# for url in urls[1050:1100]:
# for url in urls[1100:1150]:
# for url in urls[1150:1200]:
# for url in urls[1200:1250]:
# for url in urls[1250:1300]:
# for url in urls[1300:1350]:
for url in urls[1350:1400]:
        cmd = "google-chrome %s" % url
        os.system(cmd)
        time.sleep(1)
        t = t + 1
        # if(t%10 == 0):
        #         time.sleep(10)
os.system("google-chrome https://github.com/algoboy101/note_blog_comment/issues?page=1&q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc")