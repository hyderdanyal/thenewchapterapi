from flask import Flask,json,jsonify,request,Response
import json
import pandas as pd
from flask_cors import CORS
from authorbased import *
from tagbased import *
from timebased import *
from ratingbased import *
from RecommendationMF import *
app = Flask(__name__)
CORS(app)


@app.route("/authorbased")
def index():  

   title = request.args.get('Title')
   data=authorbased(title)
#    dataset=jsonify(data)
   # print((data))
   # json_data=json.dumps(data)
   # print(json_data)
   # print(type(json_data))
   resp=Response(data,status=200,mimetype='application/json')
   return jsonify(data)
   

@app.route("/tagbased")
def tags():
   title = request.args.get('Title')
   data=tagbased(title)
   return jsonify(data)

@app.route("/timebased")
def time():
#    title = request.args.get('Title')
   data=timebased()
   return jsonify(data)

@app.route("/ratingbased")
def rating():
   data=ratingbased()
   return jsonify(data)   

@app.route("/matrixfactorization")
def recommend():
    uid=request.args.get('uid')
    data=Recommendation(uid)
    return jsonify(data)
if __name__ == " __main__ ":
    app.run(debug=True)
