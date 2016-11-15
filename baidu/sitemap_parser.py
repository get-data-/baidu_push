# -*- coding: utf-8 -*-
"""
Authors: Kevin Tarvin | Eric Watson
"""

import sys
import urllib
import requests
import tldextract
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urlparse

'''
usage
$ python sitemap_parser.py "url_of_sitemap"
'''

def nameParser(url):
    '''Parse a URL and return the domain name as a string'''

    if isinstance(url, str):
        client = tldextract.extract(url)
        return str(client.domain)
    else:
        return str("Invalid client name")

def fetchsite(url):
    '''Creates a BeautifulSoup object from the input URL'''
    
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html5lib')
    return soup

def main(argv):
    '''Parse an xml sitemap and return a csv with percent encoded URLs'''

    soup = fetchsite(argv[0])
    urls = soup.findAll('url')
    if not urls:
        raise SystemExit("No Urls in Sitemap Input")
    
    out = []
    
    for url in urls:
        loc = url.find('loc').string
        parsed_url = urlparse(loc)
        path = parsed_url.path
        encoded_url = "%s://%s%s" % (parsed_url.scheme, parsed_url.netloc, urllib.parse.quote(path))
        out.append(encoded_url)
    data = {"URLs": out}
    df = pd.DataFrame(data)
    fname = nameParser(out[0])
    df.to_csv("%s.csv" % (fname))
        

if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except Exception as e:
        raise SystemExit(e)
