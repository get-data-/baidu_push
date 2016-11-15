# -*- coding: utf-8 -*-
import tldextract

def nameParser(url):
    '''Parse a URL and return the domain name'''

    if isinstance(url, str):
        client = tldextract.extract(url)
        return str(client.domain)
    else:
    	return str("Invalid Input")