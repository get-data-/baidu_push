# -*- coding: utf-8 -*-
"""
File output by Eric Watson (https://github.com/Edubya77)
"""

from bs4 import BeautifulSoup
import requests

outfile = 'output.txt'
ofile = open(outfile,"w")
loc = []


def fetchsite(url):
    '''Creates a BeautifulSoup object from the input URL'''
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    return soup

def main():
    soup = fetchsite("http://zh.rebeccaminkoff.com/sitemaps/www.rebeccaminkoff.com/sitemap.xml")
    urls = soup.findAll('url')
    if not urls:
        return False
    
    out = []
    
    for url in urls:
        loc = url.find('loc').string
        out.append(loc.encode("utf8"))
        
    for i in out:
        print(i)
        ofile.write(i + "\n")    

if __name__ == '__main__':
    main()