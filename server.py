from flask import Flask

app = Flask(__name__,
            static_url_path='',
            static_folder='static')

app.run(debug=True)

@app.route('/')
def about():
    f = open("data/data.json","r")
    
