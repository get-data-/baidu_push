# -*- coding: utf-8 -*-
import os
from flask import Flask
from config import configure_app

app = Flask(__name__)

app.config.from_object("config.DevelopmentConfig")
configure_app(app)


import baidu.views