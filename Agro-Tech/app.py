
from flask import Flask, render_template, request, redirect, url_for, session,flash
import sqlite3
from routes import routes 

app = Flask(__name__)

app.secret_key = 'key' 


app.register_blueprint(routes) 

def init_db():
    conn = sqlite3.connect('agrodata.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            city TEXT NOT NULL,
            state TEXT,
            zip TEXT               
        )
    ''')
    conn.commit()
    conn.close()


@app.route('/')
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
