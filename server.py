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

    brkbirdnum=0
    brnxbirdnum=0
    qubirdnum=0
    manbirdnum=0
    sibirdnum=0
    for borough in data:
        for call in data[borough]:
            if borough== "Manhattan":
                manbirdnum+=(data[borough][call][4])/200
            elif borough== "Bronx":
                brnxbirdnum+=(data[borough][call][4])/200
            elif borough=="Queens":
                qubirdnum+=(data[borough][call][4])/200
            elif borough == "Staten Island":
                sibirdnum+=(data[borough][call][4])/200
            elif borough=="Brooklyn":
                brkbirdnum+=(data[borough][call][4])/200
    print(brkbirdnum,manbirdnum,qubirdnum,sibirdnum,brnxbirdnum)

    return render_template("macro.html",boroughs= data.keys(),brkbirdnum=brkbirdnum,manbirdnum=manbirdnum,qubirdnum=qubirdnum,sibirdnum=sibirdnum,brnxbirdnum=brnxbirdnum)

@app.route('/about')
def about():
    f = open("data/data.json","r")
    data=json.load(f)
    return render_template('about.html',boroughs=data.keys())


@app.route('/borough')
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