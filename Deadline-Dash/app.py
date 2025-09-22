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

@app.route('/add_exam', methods=['POST'])
def add_exam():
    # 1. Check if a user is logged in by looking for 'user_id' in the session
    if 'user_id' not in session:
        
        return redirect(url_for('login'))

    # 2. Get the form data
    exam_name = request.form.get('exam_name')
    exam_date = request.form.get('exam_date')
    user_id = session['user_id']

    # 3. Validate that the data is not empty
    if not exam_name or not exam_date:
        
        return redirect(url_for('home')) # Or wherever your form is

    # 4. Connect to the database and insert the new exam
    conn = sqlite3.connect('dash.db')
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO exam (Exm_name, Exm_date, uid) VALUES (?, ?, ?)',
        (exam_name, exam_date, user_id)
    )
    conn.commit()
    conn.close()

    
    return redirect(url_for('home'))

@app.route('/profile')
def profile():
    # Check if the user is logged in
    if 'user_id' not in session:
        
        return redirect(url_for('login'))

    user_id = session['user_id']

    # Fetch user data from the database
    conn = sqlite3.connect('dash.db')
    cursor = conn.cursor()
    cursor.execute('SELECT uid, Uname, email FROM user WHERE uid = ?', (user_id,))
    user_data = cursor.fetchone() # Fetches one user
    conn.close()

    if user_data:
        # Pass the user data tuple to the template
        return render_template('profile.html', user=user_data)
    else:
        # If user not found (e.g., deleted), clear session and redirect
        
        session.clear()
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user_id', None) # Remove user_id from session
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)