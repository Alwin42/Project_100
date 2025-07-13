
from flask import Flask, render_template, request, redirect, url_for, session


app = Flask(__name__)

app.secret_key = 'key' 
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
