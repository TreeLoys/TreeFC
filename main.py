#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TreeLoys at 28.10.2020

from flask import Flask, render_template, jsonify, request
from qtviewer import flaskrun
import explorer
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

te = explorer.TreeExplore()


@app.route("/")
def main():
    return render_template("main.html")


@app.route("/gets-disk")
def getDisk():
    response = jsonify(te.generateObjectForJsonify())
    return response

@app.route("/click-browse", methods=["GET", "POST"])
def clickOnNode():
    # TODO реализовать данный метод, чтобы можно было по дереву перемещаться
    data = request.get_json(force=True)
    fullpath = data['fullpath']
    print(fullpath, "Fullpath")
    response = jsonify(te.click(fullpath))
    return response

if __name__ == "__main__":
    "Create the main window"
    flaskApp = flaskrun.appRun(app, title="TreeFC", port=5050)
