# -*- coding: utf-8 -*-

import requests
import datetime
import tldextract
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import quote_plus


def nameParser(url):
    '''Parse a URL and return the domain name'''

    if isinstance(url, str):
        client = tldextract.extract(url)
        return str(client.domain)
    else:
        return str("Invalid Input")

def fetchsite(url):
    '''Creates a BeautifulSoup object from the input URL'''
    
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html5lib')
    return soup
    
def encodeUrl(url):
    '''Taking program data and make it safe for use as URL components by 
    quoting special characters and appropriately encoding non-ASCII text'''

    encodedUrl = quote_plus(url)
    return encodedUrl

def parseSitemapUrls(sitemapUrl):
    '''Parse an xml sitemap and return a csv with percent encoded URLs'''

    soup = fetchsite(sitemapUrl)
    urls = soup.findAll('url')
    if not urls:
        #raise SystemExit("No Urls in Sitemap Input")
        pass
    out = []
    for url in urls:
        loc = url.find('loc').string
        encoded_url = encodeUrl(loc)
        out.append(encoded_url)
    return out

# def makeDocument(parsedLoc):
#     '''Take a parsed sitemap URL and create a mongo document'''

#     client = nameParser(parsedLoc)
#     date = datetime.datetime.today().strftime("%Y-%m-%d")
#     doc = {"client":client, "date":date, "sitemap_url":parsedLoc}
#     return doc

def prepSiteUrl(url):
    '''Create a string value of the website to append to Baudu link submission endpoint'''

    tld = tldextract.extract(url)
    #grab subdomain, domain, and suffix
    site = ".".join(tld[:3])
    return site

def prepPush(site, client_token):
    '''Build the endpoint where URLs will be submitted to Baidu'''

    baiduUrl = 'http://data.zz.baidu.com/urls'
    baiduSubmissionUrl = '%s?site=%s&token=%s' % (baiduUrl, site, client_token)
    return baiduSubmissionUrl

def prepData(urlList, nPush):
    '''Slices a list of URLs and returns a plain text string of URLs separated by a new line'''

    if nPush > 2000 or nPush <= 0:
        pass
    else:
        if len(urlList) < nPush: #Daily limit of URLs pushed to Baidu is 2000
            data = "\n".join(urlList)
            return data
        else:
            maxLimit = nPush + 1
            newUrlList = urlList[:maxLimit]
            data = "\n".join(newUrlList)
            return data

def prepRequest(urlList, client_token, nPush):
    '''Makes a post request to Baidu to submit URLs to its crawler'''
    headers={'content-type':'text/plain'}
    site = prepSiteUrl(urlList[0])
    print(site,"\n","\n")
    data = prepData(urlList, nPush)
    print(data)
    baiduSubmissionUrl = prepPush(site, client_token)
    r = requests.post(baiduSubmissionUrl, headers = headers, data = data)
    return r.text