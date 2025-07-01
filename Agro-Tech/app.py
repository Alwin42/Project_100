from flask import Flask,render_template,request , redirect, url_for , session

app = Flask(__name__)

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

        user=users.get(username)
        if user and user['password'] == password:
            return redirect(url_for('dashboard'))
        else:
            return "Invalid Username or Password",401
    
    return render_template('login.html')


users= {
    'Alwin':
    {
        'password': "1234",
        'email': "alwin@gmail.com"
    },

    'Admin':
    {
        'password': "admin123",
        'email': "admin123@gmail.com"
    }
}

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']
    user = users[username]
    return render_template('dashboard.html', username=username, email=user['email'])

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
