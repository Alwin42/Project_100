from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user 

# App Configuration 
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotel.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = 'your_secret_key'



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
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))



@app.route('/dashboard')
@login_required
def dashboard():
    
    return render_template('dashboard.html')

@app.route('/register', methods=['GET', 'POST'])
def register():        
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)