from flask import Flask, render_template, request, redirect, url_for, session,flash
import sqlite3
from routes import routes 

app = Flask(__name__)

app.secret_key = 'key' 
app.register_blueprint(routes) 

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)