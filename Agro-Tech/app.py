
from flask import Flask, render_template, request, redirect, url_for, session,flash
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
            name TEXT NOT NULL, username TEXT NOT NULL, password TEXT NOT NULL,
            city TEXT NOT NULL,zip TEXT NOT NULL,
            state TEXT NOT NULL, role TEXT NOT NULL DEFAULT 'user'
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
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    name = db.Column(db.String(150))
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    zip = db.Column(db.String(10))
    role = db.Column(db.String(50), default='user')

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
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['username'] = user.username
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']
    return render_template('dashboard.html', username=username,)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/profile')
def profile():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    user = User.query.filter_by(username=session['username'].first())
    return render_template('profile.html',username=user.username,password=user.password,name=user.name,city=user.city,state=user.state,zip=user.zip)

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
    if request.method == 'POST':
        new_user = User(username=request.form['username'],
                        password=request.form['password'],
                        name=request.form['name'],
                        city=request.form['city'],
                        state=request.form['state'],
                        zip=request.form['zip'])
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.')
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
