# -*- coding: utf-8 -*-
from wtforms import Form, StringField, validators, IntegerField

class SitemapForm(Form):
    sitemapUrl = StringField(u'Enter a website', [validators.required(), validators.URL(require_tld=True, message=u'Invalid URL.')])