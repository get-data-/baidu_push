# -*- coding: utf-8 -*-

from wtforms import Form
from wtforms import validators
from wtforms import StringField
from wtforms import IntegerField
from wtforms import SubmitField

class SitemapForm(Form):
    sitemapUrl = StringField(u'Enter a Sitemap', [validators.required(), validators.URL(require_tld=True, message=u'Invalid URL.')])
    submit = SubmitField("Register Client")
	
class PushForm(Form):
	token = StringField(u'Baidu Webmaster Token', [validators.required(), validators.length(max=20)])
	nPush = IntegerField('Number of URLs to Submit', [validators.required(), validators.NumberRange(min=0, max=2000)])
	submit = SubmitField("Baidu Push!")