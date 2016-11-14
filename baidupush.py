# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 15:17:45 2016
Created by Ryan Chooai (https://chineseseoshifu.com/blog/submit-urls-to-baidu-in-style.html)
Modified by Eric Watson (https://github.com/Edubya77)
"""

import requests

seed_file = open('urls.txt', 'r')
urllist = '\n'.join(seed_file.readlines())

r = requests.post(
"http://data.zz.baidu.com/urls?site=abc.com&token=enterhere",
data=urllist,
headers={'content-type':'text/plain'})

print (r.text)