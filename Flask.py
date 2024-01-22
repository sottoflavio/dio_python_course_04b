!pip install flask_ngrok

import pandas as pd
from flask_ngrok import run_with_ngrok
from flask import request, jsonify, Flask
import random as rk

app = Flask(__name__)
run_with_ngrok(app)

d = {
      "number": 1,
      "Name": "Mahesh",
      "Age": 22,
      "City":"Bangalore",
      "Country":"India"
      ,
      "number": 2,
      "Name": "Alex",
      "Age": 26,
      "City":"London",
      "Country":"England"
      ,
      "number": 3,
      "Name": "David",
      "Age": 27,
      "City":"San Francisco",
      "Country":"USA"
      
}

@app.route("/")
def home():
  return "<marquee><h3> TO CHECK IN PUT ADD '/input' TO THE URL AND TO CHECK PUT ADD '/output' TO THE URL </h3></marquee>"

@app.route("/input")
def input():
  return jsonify(d)

@app.route("/output")
def predJson():
  pred = r.choise["Positivo","Negativo"]
  nd = d
  nd["prediction"]=pred
  return jsonify(nd)

app.run
