import subprocess
import requests
from flask import Flask, render_template, url_for, request
import nmap
import xmltodict
from json2html import *
import json
import os
import pandas as pd


app = Flask(__name__)
#app.add_url_rule('/', 'index', /index.html)
#app.add_url_rule('/result', methods=['POST'], iporhost)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/doc')
def document():
    return render_template("doc.html")

@app.route('/result', methods=['POST', 'GET'])
def result():
    #target_ip = request.form('target_ip')
    #command = 'nmap -p- 127.0.0.1 --script=vuln -oX templates/results.xml'
    if request.method=="POST":
        BASE = "http://172.105.57.131:5010/"
        item = request.form['iporhost']
        type(item)
        opt = int(request.form['profile'])

        if opt is 1:
            response = requests.get(BASE + "api/p1/{}".format(item))
        elif opt is 2:
            response = requests.get(BASE + "api/p2/{}".format(item))
        elif opt is 3:
            response = requests.get(BASE + "api/p3/{}".format(item))
        elif opt is 4:
            response = requests.get(BASE + "api/p4/{}".format(item))
        else:
            response = requests.get(BASE + "api/p5/{}".format(item))
        json_data = response.json()
        html_data = json2html.convert(json = json_data)
        with open("C:\\bin\PCL\\test\\flask_test_web\\templates\\results.html", "w") as result:
            result.write(html_data)
        return render_template("results.html", title='result')

    else:
        return render_template("results.html", title='result')

@app.route('/scanner')
def scanner():
    return render_template("scanner.html", title='scanner')

app.run(debug=True)
