from flask import Flask, request, redirect, render_template, session
from flask_sqlalchemy import SQLAlchemy
import hashlib
import statistics
import matplotlib.pyplot as plt

from models import (bar_chart, check_signup, check_user, data_number_check, enter_data, get_data, get_mean, get_median, get_mode, get_set,
get_standard_deviation, get_variance, logout_user, separate_data, create_user)


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://stats:password@localhost:8889/stats'
db = SQLAlchemy(app)

app.secret_key = 'y337kGcys&zP3B'

class Data(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    data = db.Column(db.String(120))

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
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        # check_user either returns true or a dict with an error message.
        user = check_user(request.args.get('username'),request.args.get('password'))
        if user:
            session['username'] = request.args.get('username')
            return redirect('/data')
        else:
            return render_template('/login', user=user)
    else:
        user = {'password_error': '', 'username_error':''}
        return render_template('login.html', user=user)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        #check_signup either returns true or a dict with an error message.
        user = check_signup(request.form.get('username'), request.form.get('password'), request.form.get('verify'))
        if user:
            create_user(request.form.get('username'), request.form.get('password'))
            session['username'] = request.form.get('username')
            return redirect('/newdata')
        else:
            return render_template('signup.html', user=user)
    else:
        user = {'password_error':'', 'user_error':''}
        return render_template('signup.html', user=user)

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        check_number = data_number_check(request.form.get('data'))
        if check_number:
            enter_data(request.form.get('data'))
            return redirect('/my_data')
        else:
            return render_template('data.html', error='Please follow the format for entering data.')
    return render_template('data.html')

@app.route('/my_data', methods=['GET', 'POST'])
def my_data():
    if request.args.get('entry_id'):
        data_set = get_set(request.args.get('entry_id'))
        # the data set is in csv format and needs to be broken up into a list to use.
        data = separate_data(data_set)
        mean = get_mean(data)
        median = get_median(data)
        mode = get_mode(data)
        variance = get_variance(data)
        standard_deviation = get_standard_deviation(data)
        graph = bar_chart(data)
        return render_template('dataset.html', data=data, mean=mean, median=median, mode=mode, variance=variance,
         standard_deviation=standard_deviation, graph=graph)
    else:
        data_sets = get_data(session['username'])
        return render_template('my_data.html', data_sets=data_sets)

@app.route('/logout', methods=['GET'])
def logout():
    logout_user(request.session.get(username))
    return redirect('/login')

if __name__ == '__main__':
    app.run()