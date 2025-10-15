from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
from datetime import datetime, date


app = Flask(__name__)
app.secret_key = 'secret_key'

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE user (
                uid INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL ,
                password TEXT NOT NULL,
                phone TEXT NOT NULL,
                reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                
            );
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    return render_template('booking.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM user WHERE email=? AND password=?', (email, password))
        user_details = cursor.fetchone()
        conn.close()
        if user_details:
            session['email'] = user_details[1]  
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/logout')

def logout():
    
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))



@app.route('/register', methods=['GET', 'POST'])
def register():        
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)