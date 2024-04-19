from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__,
            static_url_path='',
            static_folder='static')



@app.route('/')
def macro():
    f = open("data/data.json","r")
    return render_template("macro.html")

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/micro')
def micro():
    borough = request.args.get('borough')
    return render_template('micro.html', borough=borough)

@app.route('/extrainfo')
def extrainfo():
    return render_template('extrainfo.html')
   
app.run(debug=True)