#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TreeLoys at 28.10.2020

from flask import Flask, render_template, jsonify
from qtviewer import flaskrun

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("main.html")


@app.route("/gets-disk")
def getDisk():
    response = jsonify([{"text":"C:"}])
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == "__main__":
    "Create the main window"
    flaskApp = flaskrun.appRun(app, title="TreeFC", port=5050)
