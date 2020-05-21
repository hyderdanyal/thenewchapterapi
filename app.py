from flask import Flask, json, jsonify, request, Response
import json
import pandas as pd
from flask_cors import CORS
from authorbased import *
from tagbased import *
from timebased import *
from ratingbased import *
from RecommendationMF import *
from genre import *
from search import *
from searchpage import *
from feedback import *
# from connectfirebase import *

app = Flask(__name__)
CORS(app)
app.debug = True


@app.route("/authorbased")
def index():

    title = request.args.get('Title')
    data = authorbased(int(title))

    return jsonify(data)


@app.route("/tagbased")
def tags():
    title = request.args.get('Title')
    data = tagbased(int(title))
    return jsonify(data)


@app.route("/timebased")
def time():

    data = timebased()
    return jsonify(data)


@app.route("/ratingbased")
def rating():
    data = ratingbased()
    return jsonify(data)


@app.route("/matrixfactorization")
def recommend():
    uid = request.args.get('uid')

    data = Recommendation(uid)
    return jsonify(data)


@app.route("/genre")
def bookgenre():
    gen = request.args.get('genre')
    data = genre(gen)
    return jsonify(data)


@app.route("/search")
def search():
    searchvalue = request.args.get('q')
    data = searchbook(searchvalue)
    return jsonify(data)


@app.route("/searchresult")
def searchresult():
    searchvalue = request.args.get('q')
    data = searchpage(int(searchvalue))
    return jsonify(data)


@app.route("/feedback")
def email():
    name = request.args.get('name')
    email = request.args.get('email')
    msg = request.args.get('msg')
    feedback(msg, name, email)
    return jsonify('Mail Sent')


if __name__ == " __main__ ":
    app.run(debug=True)
