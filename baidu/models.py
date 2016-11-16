# -*- coding: utf-8 -*-

from wtforms import Form
from wtforms import validators
from wtforms import StringField
from wtforms import IntegerField

class SitemapForm(Form):
    sitemapUrl = StringField(u'Enter a website', [validators.required(), validators.URL(require_tld=True, message=u'Invalid URL.')])
	
class PushForm(Form):
	token = StringField(u'Enter Baidu token', [validators.required(), validators.length(max=10)])
	nPush = IntegerField('Country Code', [validators.required(), validators.NumberRange(min=0, max=2000)])
	# client = StringField(u'Enter Baidu client', [validators.required(), validators.URL(require_tld=True, message=u'Invalid token')])