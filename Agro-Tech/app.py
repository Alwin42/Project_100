from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_super_secret_key' 
users = {
    'Alwin': {
        'password': "1234",
        'email': "alwin@gmail.com",
        'First name': "Alwin",
        'Last name': "Emmanuel",
        'Username': "Alwin42",
        'City': "Ernakulam",
        'State': "Kerala",
        'Zip': "682020",
    },
    'Admin': {
        'password': "admin123",
        'email': "admin123@gmail.com"
    }
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
    if 'username' not in session:
        return redirect(url_for('login'))
    username = session['username']
    user = users.get(username)
    return render_template('profile.html', username=username, email=user['email'],FirstName=user['First name'],LastName=user['Last name'] ,
                           Username=user['Username'], City=user['City'], State=user['State'], Zip=user['Zip'])

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

@app.route('/payment')
def payment():
    if 'username' not in session:
        return redirect(url_for('login'))
    username = session['username']
    return render_template('payment.html', username=username)

@app.route('/seller')
def seller():
    return render_template('seller.html')

if __name__ == '__main__':
    app.run(debug=True)
