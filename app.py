from controller import get_data

from flask import Flask
from flask import request, jsonify,render_template

from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = True
app.static_folder = 'static'
@app.route('/api/')
def index():
    url=request.args.get('url')
    data=get_data(url) 
    return data

@app.route('/')
def home():
    return render_template("index.html")
