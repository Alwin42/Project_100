from flask import Flask, render_template , url_for , request, redirect, session
import sqlite3
import datetime
app = Flask(__name__)
app.secret_key = 'haha_secret_key'
def init_db():
    conn = sqlite3.connect('dash.db')
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE user (
                uid INTEGER PRIMARY KEY AUTOINCREMENT,
                Uname TEXT NOT NULL,
                email TEXT NOT NULL ,
                password TEXT NOT NULL
            );
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect('dash.db')
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM user WHERE email = ? AND password = ?''', (email, password))

        user = cursor.fetchone()
        conn.close()

        if user:
            session['user_id'] = user[0]
            return redirect(url_for('home'))
        else:
            return "<h1>Invalid credentials. Please try again.</h1>"
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['Uname']
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect('dash.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO user (Uname, email, password)
            VALUES (?, ?, ?)''', (username, email, password))

        conn.commit()
        conn.close()

        return redirect(url_for('login'))

    
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)