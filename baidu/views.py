# -*- coding: utf-8 -*-
import datetime
from baidu import app
import json
from flask import render_template, jsonify, request, session, redirect, url_for, abort, Response
from flask.ext.pymongo import PyMongo
from baidu.compute import nameParser
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
        except Exception as e:
            pass
        return redirect(url_for("baiduIndex"))
    elif request.method == 'POST' and mod== "edit":
        return render_template("push.html")
    else:
        return redirect(url_for("baiduIndex"))
        
@app.route("/baidu/clients/action/push/", methods=["GET", "POST"])
def push():
    form = PushForm(request.form)
    return render_template("push.html", form=form)
    if request.method == "POST" and form.validate():
        token = form.token.data
        client = form.client.data
        number = form.number.data
        try:
            pass #make the main push function run here
        except Exception as e:
            pass
        return redirect(url_for("baiduIndex"))
    else:
        return redirect(url_for("baiduIndex"))

@app.route("/historic_api_created")
def historic_api_created():
    #query DB to get his format for the URLs saved to the database over time
    data = [{"yAxis": "1", "key": "Serie 1", "values": [{"x": "Sun", "y": 73}]}]
    return Response(json.dumps(data), 201, mimetype="application/json")
    
@app.route("/historic_api_pushed")
def historic_api_pushed():
    #query DB to get his format for the URLs pushed to Baidu over time
    data = [{"yAxis": "1", "key": "Serie 1", "values": [{"x": "Sun", "y": 56},{"x": "Mon", "y": 60}]}]
    return Response(json.dumps(data), 201, mimetype="application/json")            