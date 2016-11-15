# -*- coding: utf-8 -*-
import os
import logging

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = ''
    MONGO_DBNAME = ''
    MONGO_URI = ''
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = 'baidu.log'
    LOGGING_LEVEL = logging.DEBUG

class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = ''

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SECRET_KEY = ''

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SECRET_KEY = 'This-should-get-updated'

class TestingConfig(Config):
    TESTING = True

def configure_app(app):
    # Logging Configuration
    handler = logging.FileHandler(app.config['LOGGING_LOCATION'])
    handler.setLevel(app.config['LOGGING_LEVEL'])
    formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)