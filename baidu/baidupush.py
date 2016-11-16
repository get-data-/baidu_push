# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 15:17:45 2016
Created by Kevin Tarvin | Eric Watson
"""

import sys
import time
import requests
import pandas as pd
import tldextract

def readUrlList(csvfilename):
    df = pd.read_csv(csvfilename)
    return df

def prepSiteUrl(url):
    tld = tldextract.extract(url)
    #grab subdomain, domain, and suffix
    site = ".".join(tld[:3])
    return site

def prepPush(site, client_token):
    baiduUrl = 'http://data.zz.baidu.com/urls'
    baiduSubmissionUrl = '%s?site=%s&token=%s' % (baiduUrl, site, client_token)
    return baiduSubmissionUrl

def main(argv):
    output = []
    df = readUrlList(argv[0])
    headers={'content-type':'text/plain'}
    site = prepSiteUrl(df['URLs'][0])
    client_token = argv[1]
    baiduSubmissionUrl = prepPush(site, client_token)
    if len(df.index) > 2000: #Daily limit of URLs pushed to Baidu is 2000
        df2 = df.head(2000)
        for i in df2.index:
            url = df2['URLs'][i]
            output.append(url)
        df2.to_csv("submitted.csv")
    else:
        for i in df.index:
            url = df['URLs'][i]
            output.append(url)
        df.to_csv("submitted.csv")
    urlList = "\n".join(output)
    r = requests.post(baiduSubmissionUrl, headers = headers, data = urlList)
    print(r.text)

if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except Exception as e:
        raise SystemExit(e)