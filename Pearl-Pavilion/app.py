from flask import Flask, render_template, request, redirect, url_for, flash

# App Configuration
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    return render_template('booking.html')

if __name__ == '__main__':
    app.run(debug=True)