
from flask import Flask, render_template, request, redirect, url_for, session,flash
import sqlite3


app = Flask(__name__)

app.secret_key = 'key' 
def init_db():
    conn = sqlite3.connect('agrodata.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            city TEXT NOT NULL,
            state TEXT NOT NULL,
            zip TEXT NOT NULL              
        )
    ''')
    conn.commit()
    conn.close()


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

        with sqlite3.connect('agrodata.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
            user = cursor.fetchone()

            if user:
                session['user'] = {
                    'id': user[0],
                    'name': user[1],
                    'username': user[2],
                    'city': user[4],
                    'state': user[5],
                    'zip': user[6]
                }
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid username or password', 'error')
                
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
    
    
    return render_template('profile.html')

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
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']
        city = request.form['city']
        state = request.form['state']
        zip_code = request.form['zip']
        role = request.form['role']

        with sqlite3.connect('agrodata.db') as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('''
                    INSERT INTO users (name,username,password,city,
                               state,role) VALUES (?,?,?,?,?,? )''')
                conn.commit()
                flash('Registration successful!', 'success')
                return redirect(url_for('login'))
            except sqlite3.IntegrityError:
                flash('Username already exists. Please choose a different one.', 'error')
                return redirect(url_for('register'))
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
