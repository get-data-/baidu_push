# -*- coding: utf-8 -*-
import datetime
from baidu import app
from flask import render_template, jsonify, request, session, redirect, url_for, abort
from flask.ext.pymongo import PyMongo

mongo = PyMongo(app)


@app.route('/')
def homepage():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    app.logger.error('Page not found: %s', (request.path, error))
    return render_template('400.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error('Server Error: %s', (error))
    return render_template('500.html'), 500