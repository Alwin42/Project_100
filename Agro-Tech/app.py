from datetime import datetime, timezone
from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = 'key' 

DB_PATH = "/home/alwin42/Programs/Projects_100/Agro-Tech/agrodata.db"
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_PATH}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
def init_db():
    conn =sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Get all users from the databse
def get_users():
    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return users

# Add a user to the database
def add_user(name, age):
    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)',(name, age))
    conn.commit()
    conn.close()

# Update user's details
def update_user(id, name, age):
    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()
    cursor.execute('UPDATE users SET name = ?, age = ? WHERE id = ?',(name, age, id))
    conn.commit()
    conn.close()

# Delete a user by ID
def delete_user(id):
    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = ?', (id,))
    conn.commit()
    conn.close()
users = {
    'Alwin': {
        'username': 'Alwin',
        'password': 'apple222',
        'email': 'john@gmail.com',
        'first_name': 'Alwin',
        'last_name': 'Emmanuel',
        'city': 'Kochi',
        'state': 'Kerala',
        'zip': '682001'
    },
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/crops')
def crops():
    return render_template('crops.html')

@app.route('/marketplace')
def marketplace():
    return render_template('marketplace.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = users.get(username)
        if user and user['password'] == password:
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return "Invalid Username or Password", 401

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']
    user = users.get(username)
    return render_template('dashboard.html', username=username, email=user['email'])

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/profile')
def profile():
    username = session['username']
    user = users.get(username)
    return render_template(
        'profile.html',
        username=user['username'],
        first_name=user['first_name'],
        last_name=user['last_name'],
        city=user['city'],
        state_selected=user['state'],
        zip=user['zip']
    )

@app.route('/cart')
def cart():
    if 'username' not in session:
        return redirect(url_for('login'))
    username = session['username']
    return render_template('cart.html')

@app.route('/orders')
def orders():
    if 'username' not in session:
        return redirect(url_for('login'))
    username = session['username']
    return render_template('orders.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@app.route('/payment')
def payment():
    if 'username' not in session:
        return redirect(url_for('login'))
    username = session['username']
    return render_template('payment.html', username=username)

@app.route('/receipts')
def receipts():
    return render_template('receipts.html')

@app.route('/seller')
def seller():
    return render_template('seller.html')

if __name__ == '__main__':
    app.run(debug=True)
