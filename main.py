from flask import Flask, request, redirect, render_template, session
from flask_sqlalchemy import SQLAlchemy
import hashlib
import statistics
import matplotlib.pyplot as plt

import controller
import model


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://stats:stats@localhost:8889/stats'
db = SQLAlchemy(app)
app.secret_key = 'y337kGcys&zP3B'

class Data(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    data = db.Column(db.String)

    def __init__(self, data):
        self.data = data

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120))
    password_hash = db.Column(db.String(120))
    data = db.relationship('Data', backref='user')

    def __init__(self, username, password_hash):
        self.username = username
        self.password_hash = password_hash

@app.before_request
def require_login():
    allowed_routes = ['login', 'signup']
    if request.endpoint not in allowed_routes and 'username' not in session:
        return redirect('/login')

@app.route('/', methods=['GET'])
controller.index()

@app.route('/login', methods=['GET','POST'])
login()

@app.route('/signup', methods=['GET'])
signup()

@app.route('/data', methods=['GET', 'POST'])
data()

@app.route('/my_data', methods=['GET', 'POST'])
my_data()

@app.route('/logout', methods=['GET'])
logout()