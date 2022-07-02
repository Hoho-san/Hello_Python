from flask import Flask, render_template, request
from flask.scaffold import _matching_loader_thinks_module_is_package

from forms import SignUpForm
app = Flask(__name__)

import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY # or random string, and you dont need the import os


# list dictionary for file 
post_list = [{"My_car1": "car 1", "brand": "Ford","model": "Mustang","year": 1964}, {"My_car2": "car 2", "brand": "suzuki","model": "d-max","year": 2020}]

@app.route('/') 
def home():
        # to choose file what to render
    return render_template('home.html')

@app.route('/animal')
def animal():
    # to choose file what to render
    return render_template('animal.html', post_list= post_list, title= 'Cars')

@app.route('/signup', methods= ["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        return render_template("userdata.html", result= result)
    return render_template('signup.html', form= form)