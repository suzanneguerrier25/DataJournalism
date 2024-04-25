from flask import Flask
from flask import render_template
from flask import request
import json


app = Flask(__name__,
            static_url_path='',
            static_folder='static')



@app.route('/')
def macro():
    f = open("data/data.json","r")
    data=json.load(f)
    return render_template("macro.html",boroughs= data.keys())

@app.route('/about')
def about():
    f = open("data/data.json","r")
    data=json.load(f)
    return render_template('about.html',boroughs=data.keys())


@app.route('/micro')
def micro():
    borough = request.args.get('borough')
    bronx=False
    if borough == "Bronx":
        bronx=True
    f = open("data/data.json","r")
    data=json.load(f)
    return render_template('micro.html', borough=borough, bronx = bronx, boroughs=data.keys())

@app.route('/extrainfo')
def extrainfo():
    f = open("data/data.json","r")
    data=json.load(f)
    return render_template('extrainfo.html',boroughs=data.keys())
   
app.run(debug=True)