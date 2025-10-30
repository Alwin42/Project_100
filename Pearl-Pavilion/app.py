from flask import Flask, render_template, request, redirect, url_for, flash, session, g
import sqlite3
import click
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, date

app = Flask(__name__)
app.secret_key = 'alwin_secret' # Change this to a real secret key
DATABASE = 'database.db'



def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(e=None):
    """Closes the database connection at the end of the request."""
    db = g.pop('db', None)
    if db is not None:
        db.close()

# --- Database Initialization ---

def init_db():
    
    db = get_db()

    # Drop tables if they exist (for easy re-initialization)
    db.execute('DROP TABLE IF EXISTS user')
    db.execute('DROP TABLE IF EXISTS Room')
    db.execute('DROP TABLE IF EXISTS Booking')

    # Create User Table
    db.execute('''
        CREATE TABLE user (
            uid INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            phone TEXT NOT NULL,
            reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    ''')
    
    # Create Room Table (based on our confirmed schema)
    db.execute('''
        CREATE TABLE Room (
            RoomID INT PRIMARY KEY,
            HotelID INT,
            RoomType VARCHAR(255),
            Price DECIMAL(10,2),
            Availability BOOLEAN,
            Features TEXT,
            image_filename VARCHAR(255)
        );
    ''')

    # Create Booking Table
    db.execute('''
        CREATE TABLE Booking (
            BookingID INTEGER PRIMARY KEY AUTOINCREMENT,
            UserID INT,
            RoomID INT,
            CheckInDate DATE,
            CheckOutDate DATE,
            TotalPrice DECIMAL(10,2),
            BookingStatus VARCHAR(255),
            Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (UserID) REFERENCES user(uid),
            FOREIGN KEY (RoomID) REFERENCES Room(RoomID)
        );
    ''')
    
    # Commit the changes
    db.commit()
    print("Database initialized.")

# Command to run from the terminal: flask init-db
@app.cli.command('init-db')
def init_db_command():
    """Clears the existing data and creates new tables."""
    with app.app_context():
        init_db()
        click.echo('Initialized the database.')

# --- Main App Routes ---

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    
    db = get_db()
    
    # Fetch data for all three sections
    rooms_data = db.execute('SELECT * FROM Room WHERE RoomID BETWEEN 1 AND 8').fetchall()
    services_data = db.execute('SELECT * FROM Room WHERE RoomID BETWEEN 9 AND 12').fetchall()
    amenities_data = db.execute('SELECT * FROM Room WHERE RoomID BETWEEN 13 AND 16').fetchall()
    
    return render_template(
        'booking.html', 
        rooms=rooms_data,
        services=services_data,
        amenities=amenities_data
    )

@app.route('/contact', methods=['GET', 'POST'])
def contact():
   
    return render_template('contact.html')

# --- Authentication Routes ---

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        db = get_db()
        user = db.execute('SELECT * FROM user WHERE email = ?', (email,)).fetchone()

        
        if user and check_password_hash(user['password'], password):
            session.clear()
            session['uid'] = user['uid']
            session['username'] = user['username']
            flash('Logged in successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password. Please try again.', 'error')
            return redirect(url_for('login'))
            
    return render_template('login.html')

@app.route('/logout')
def logout():
    """Logs the user out by clearing the session."""
    session.clear()
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']

        db = get_db()
        
        # Check if user already exists
        existing_user = db.execute('SELECT * FROM user WHERE email = ?', (email,)).fetchone()
        if existing_user:
            flash('Email already registered. Please log in.', 'error')
            return redirect(url_for('login'))

        # SECURE: Hash the password before storing
        hashed_password = generate_password_hash(password)
        
        try:
            db.execute(
                'INSERT INTO user (username, email, password, phone) VALUES (?, ?, ?, ?)',
                (username, email, hashed_password, phone)
            )
            db.commit()
        except sqlite3.Error as e:
            flash(f'An error occurred: {e}', 'error')
            return redirect(url_for('register'))

        # Get the new user's details and log them in
        new_user = db.execute('SELECT * FROM user WHERE email = ?', (email,)).fetchone()
        session['uid'] = new_user['uid']
        session['username'] = new_user['username']
        
        flash('Registration successful! You are now logged in.', 'success')
        return redirect(url_for('home'))
        
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)