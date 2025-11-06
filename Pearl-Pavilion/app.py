from flask import Flask, render_template, request, redirect, url_for, flash, session, g
import sqlite3
import click
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, date
from functools import wraps


app = Flask(__name__)
app.secret_key = 'alwin_secret' # You should change this to a long, random string
DATABASE = 'database.db'


# --- Database Helper Functions ---

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

# --- Login Decorator ---
def login_required(f):
    """
    A decorator to require login for specific routes.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'uid' not in session:
            flash('You must be logged in to view this page.', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

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
        # --- Get all form data ---
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # Get the confirmation field from your HTML
        confirm_password = request.form['confirm_password'] 
        phone = request.form['phone']

        # --- Check if passwords match ---
        if password != confirm_password:
            flash('Passwords do not match. Please try again.', 'error')
            return redirect(url_for('register'))

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
        
    # This handles the GET request
    return render_template('register.html')

# --- User Dashboard & Booking Routes ---

@app.route('/dashboard')
@login_required
def dashboard():
    """Shows the user's details and their bookings."""
    db = get_db()
    
    # Get the current user's details
    user = db.execute('SELECT * FROM user WHERE uid = ?', (session['uid'],)).fetchone()
    
    if user is None:
        session.clear()
        flash('User not found. Please log in again.', 'error')
        return redirect(url_for('login'))
        
    # Get all bookings for this user, joined with room details
    bookings = db.execute('''
        SELECT * FROM Booking b
        JOIN Room r ON b.RoomID = r.RoomID
        WHERE b.UserID = ?
        ORDER BY b.CheckInDate DESC
    ''', (session['uid'],)).fetchall()
    
    # Fetch the complimentary amenities
    amenities = db.execute('SELECT * FROM Room WHERE RoomID BETWEEN 13 AND 16').fetchall()
    
    return render_template('dashboard.html', user=user, bookings=bookings, amenities=amenities)


@app.route('/vacate/<int:booking_id>', methods=['POST'])
@login_required
def vacate(booking_id):
    """Marks a booking as 'Completed' (vacated)."""
    db = get_db()
    
    result = db.execute(
        'UPDATE Booking SET BookingStatus = ? WHERE BookingID = ? AND UserID = ?',
        ('Completed', booking_id, session['uid'])
    )
    db.commit()
    
    if result.rowcount > 0:
        flash('You have successfully checked out. Thank you for staying with us!', 'success')
    else:
        flash('Could not update booking. Please contact support.', 'error')
        
    return redirect(url_for('dashboard'))


@app.route('/create_booking', methods=['POST'])
@login_required  # Protect this route
def create_booking():
    
    if request.method == 'POST':
        db = get_db()
        
        room_id = request.form['room_type']
        check_in_str = request.form['checkin']
        check_out_str = request.form['checkout']
        user_id = session['uid']

        try:
            check_in_date = datetime.strptime(check_in_str, '%Y-%m-%d')
            check_out_date = datetime.strptime(check_out_str, '%Y-%m-%d')
            
            num_days = (check_out_date - check_in_date).days
            
            if num_days <= 0:
                flash('Check-out date must be at least one day after the check-in date.', 'error')
                return redirect(url_for('booking'))

            room = db.execute('SELECT Price FROM Room WHERE RoomID = ?', (room_id,)).fetchone()
            if not room:
                flash('Selected room does not exist.', 'error')
                return redirect(url_for('booking'))
            
            room_price = room['Price']
            total_price = room_price * num_days

        except ValueError:
            flash('Invalid date format. Please try again.', 'error')
            return redirect(url_for('booking'))
        except Exception as e:
            flash(f'An error occurred during calculation: {e}', 'error')
            return redirect(url_for('booking'))

        try:
            booking_status = 'Confirmed'
            
            db.execute('''
                INSERT INTO Booking (UserID, RoomID, CheckInDate, CheckOutDate, TotalPrice, BookingStatus)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (user_id, room_id, check_in_str, check_out_str, total_price, booking_status))
            
            db.commit()

        except sqlite3.Error as e:
            flash(f'An error occurred while saving your booking: {e}', 'error')
            return redirect(url_for('booking'))

        flash('Booking successful! Your stay is confirmed.', 'success')
        return redirect(url_for('dashboard'))

    return redirect(url_for('booking'))

if __name__ == '__main__':
    app.run(debug=True)