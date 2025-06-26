from flask import Flask,render_template

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

@app.route('/weather')
def weather():
    return render_template('weather.html')

@app.route('/login')
def login():
    return render_template('Login.html')

if __name__ == '__main__':
    app.run(debug=True)
