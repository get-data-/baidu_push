# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 15:17:45 2016
Created by Kevin Tarvin | Eric Watson
"""

import sys
import time
import requests
import pandas as pd
from urllib.parse import urlparse

def readUrlList(csvfilename):
    df = pd.read_csv(csvfilename)
    return df

def prepPush(url, client_token):
    baiduUrl = 'http://data.zz.baidu.com/urls'
    preppedUrl = '%s?site=%s&token=%s' % (baiduUrl, url, client_token)
    return preppedUrl

def main(argv):
    client_token = argv[1]
    df = readUrlList(argv[0])
    headers={'content-type':'text/plain'}
    if len(df.index) > 2: #Daily limit of URLs pushed to Baidu is 2000
        df2 = df.head(2)
        for i in df2.index:
            url = df2['URLs'][i]
            urlToSubmit = prepPush(url, client_token)
            print(urlToSubmit)
            r = requests.post(urlToSubmit, headers = headers)
            time.sleep(1)
            print(r.text)
        df2.to_csv("submitted.csv")
        print(len(df2.index))
    else:
        for i in df.index:
            url = df['URLs'][i]
            urlToSubmit = prepPush(url)
            print(urlToSubmit)
            r = requests.post(urlToSubmit, headers = headers)
            time.sleep(1)
            print(r.text)
        df.to_csv("submitted.csv")
        print(len(df.index))

if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except Exception as e:
        raise SystemExit(e)