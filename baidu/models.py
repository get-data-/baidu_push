# -*- coding: utf-8 -*-
from wtforms import Form, StringField, validators, IntegerField

class SitemapForm(Form):
    sitemapUrl = StringField(u'Enter a website', [validators.required(), validators.URL(require_tld=True, message=u'Invalid URL.')])
	
class PushForm(Form):
	token = StringField(u'Enter Baidu token', [validators.required(), validators.URL(require_tld=True, message=u'Invalid token')])
	client = StringField(u'Enter Baidu client', [validators.required(), validators.URL(require_tld=True, message=u'Invalid token')])
	number = StringField(u'Enter # of URLs (<2000)', [validators.required(), validators.URL(require_tld=True, message=u'Invalid token')])