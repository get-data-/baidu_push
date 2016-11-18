# -*- coding: utf-8 -*-
import datetime
from baidu import app
import json
from flask import render_template, jsonify, request, session, redirect, url_for, abort, Response
from flask.ext.pymongo import PyMongo
from baidu.compute import nameParser, fetchsite, parseSitemapUrls, prepRequest
from baidu.models import SitemapForm, PushForm

mongo = PyMongo(app)


@app.route("/")
def homepage():
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(error):
    app.logger.error("Page not found: %s", (request.path, error))
    return render_template("400.html"), 404

@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error("Server Error: %s", (error))
    return render_template("500.html"), 500

@app.route("/baidu/clients/")
def baiduIndex():
    baidu_clients = mongo.db.baidu
    output = []
    for q in baidu_clients.find():
        output.append({"client" : q["client"], "sitemap" : q["sitemap"], "date_created" : q["date_created"]})
    return render_template("baidu_client_index.html", output=output)

@app.route("/baidu/clients/create/", methods=["GET", "POST"])
def newClient():
    form = SitemapForm(request.form)
    if request.method == "POST" and form.validate():
        client_sitemap = form.sitemapUrl.data
        name = nameParser(client_sitemap)
        clients = mongo.db.baidu
        try:
            clients.insert({"client":name,"sitemap":client_sitemap, "date_created":datetime.datetime.today().strftime("%Y-%m-%d")})
        except Exception as e:
            pass
        return redirect(url_for("baiduIndex"))
    else:
        return render_template("sitemapform.html", form=form)

@app.route('/baidu/clients/<clientName>/action/<mod>/', methods=['POST'])
def modifyClient(clientName, mod):
    if request.method == 'POST' and mod== "delete":
        clients = mongo.db.baidu
        try:
            clients.delete_one({"client":clientName})
            return redirect(url_for("baiduIndex"))
        except Exception as e:
            app.logger.error("Page not found: %s", (request.path, e))
            return redirect(url_for("baiduIndex"))
    elif request.method == 'POST' and mod== "edit":
        return redirect(url_for("push", clientName = clientName))
    else:
        return redirect(url_for("baiduIndex"))
        
@app.route("/baidu/clients/<clientName>/action/push/", methods=["GET", "POST"])
def push(clientName):
    form = PushForm(request.form)
    if request.method == "POST" and form.validate():
        client_token = form.token.data
        nPush = form.nPush.data

        clients = mongo.db.baidu
        bResponse = mongo.db.baiduResponse
        sitemapUrl = []
        for q in clients.find({"client":clientName}):
            sitemapUrl.append(q["sitemap"])
        try:
            urlList = parseSitemapUrls(sitemapUrl[0])
            response = prepRequest(urlList, client_token, nPush)
            bResponse.insert({"client":clientName, "response":response, "date":datetime.datetime.today().strftime("%Y-%m-%d")})
            return render_template("response.html", response=response)
        except Exception as e:
            app.logger.error("Page not found: %s", (request.path, e))
            return redirect(url_for("baiduIndex"))
    else:
        if form.errors:
            app.logger.error("Page not found: %s", (request.path, form.errors))
        else:
            return render_template("push.html", form=form, clientName=clientName)

@app.route('/clients/<clientName>/')
def clientPage(clientName):
    clients = mongo.db.baidu
    c = clients.find_one({"client":clientName})
    if c is not None:
        bResponse = mongo.db.baiduResponse
        responseData = []
        responses = bResponse.find({"client":clientName})
        for data in responses:
            responseData.append({"client" : data["client"], "date" : data["date"], "response" : data["response"]})
        return render_template('client_page.html', responseData=responseData, client=clientName)
    else:
        return abort(404)