
from flask import Blueprint, render_template, request, redirect, url_for, session,flash
import sqlite3

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template('index.html')

@routes.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']
        city = request.form['city']
        state = request.form['state']
        zip_code = request.form['zip']
        role = request.form['role']
        
        conn = sqlite3.connect('agrodata.db')
        cursor = conn.cursor()
        cursor.execute('''
                    INSERT INTO users (name, username, password, city, state, zip, role)
                    VALUES (?, ?, ?, ?, ?, ?, ?)''', (name, username, password, city, state, zip_code, role))
        conn.commit()
        conn.close()
        return redirect(url_for('routes.login'))
    else:
        if 'username' in session:
            return redirect(url_for('routes.dashboard'))
    
    return render_template('register.html')

@routes.route('/crops')
def crops():
    conn = sqlite3.connect('agrodata.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    crops = cursor.fetchall()
    conn.close()
    return render_template('crops.html', crops=crops)

@routes.route('/marketplace')
def marketplace():
    conn=sqlite3.connect('agrodata.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM market')
    market = cursor.fetchall()
    conn.close()
    return render_template('marketplace.html', market=market)
    

@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('agrodata.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
        user_details = cursor.fetchone()
        conn.close()
        if user_details:
            session['username'] = user_details[2]
            
            return redirect(url_for('routes.dashboard'))
        else:
            return redirect(url_for('routes.login'))
                
    return render_template('login.html')

@routes.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('routes.login'))

    username = session['username']
    return render_template('dashboard.html', username=username,)

@routes.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('routes.login'))

@routes.route('/profile')
def profile():
    if 'username' not in session:
        return redirect(url_for('routes.login'))
    
    username = session['username']
    
    conn = sqlite3.connect('agrodata.db')
    conn.row_factory = sqlite3.Row  
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user_details = cursor.fetchone()
    conn.close()

    if user_details:
       
        session['name'] = user_details['name']
        session['city'] = user_details['city']
        session['state'] = user_details['state']
        session['zip'] = user_details['zip']

        return render_template(
            'profile.html',
            username=user_details['username'],
            name=user_details['name'],
            city=user_details['city'],
            state=user_details['state'],
            zip=user_details['zip'],
            role=user_details['role']
        )
    else:
        flash('User not found', 'error')
        return redirect(url_for('routes.login'))

@routes.route('/cart')
def cart():
    if 'username' not in session:
        return redirect(url_for('routes.login'))

    username = session['username']

    conn = sqlite3.connect('agrodata.db')
    conn.execute('PRAGMA foreign_keys = ON;')  
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    
    cursor.execute('SELECT * FROM cart;')
    cart = cursor.fetchall()

    conn.close()

    return render_template('cart.html', cart=cart, username=username)

@routes.route('/cart/add', methods=['POST'])
def add_to_cart():
    if 'username' not in session:
        return redirect(url_for('routes.login'))
    pid = request.form.get('pid')
    pname = request.form.get('pname')
    pdetails = request.form.get('pdetails')
    category = request.form.get('category')
    img = request.form.get('img')
    price = request.form.get('price')
    conn = sqlite3.connect('agrodata.db')
    cursor = conn.cursor()
    
    cursor.execute(
    "SELECT pid, pname, pdetails, category, img, price FROM products WHERE pid = ?", 
    (pid,))
    product = cursor.fetchone()
    pid, pname, pdetails, category, img, price = product
    user_id=1
    if not product:
        conn.close()
        return redirect(url_for('routes.crops'))
    cursor.execute("SELECT pid, pname, pdetails, category, img, price FROM products WHERE pid = ?", (pid, ))
    product = cursor.fetchone()
    cursor.execute("""
            INSERT INTO cart (pid, user_id, pdetails, pname, quantity, category, img, price)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (pid, user_id, pdetails, pname, 1, category, img, price))

    conn.commit()
    conn.close()

    return redirect(url_for('routes.crops'))


@routes.route('/cart/delete')
def delete_from_cart():
    if 'username' not in session:
        return redirect(url_for('routes.login'))
    
    cid = request.args.get('cid')
    if not cid:
        return redirect(url_for('routes.cart'))  
    
    conn = sqlite3.connect('agrodata.db')
    cursor = conn.cursor()
    
    
    cursor.execute('DELETE FROM cart WHERE cid=?', (cid))
    
    conn.commit()
    conn.close()
    
    return redirect(url_for('routes.cart'))

@routes.route('/cart/buy')
def buy_now():
    if 'username' not in session:
        return redirect(url_for('routes.login'))
    
    cid = request.args.get('cid')
    if not cid:
        return redirect(url_for('routes.cart'))
    
    conn = sqlite3.connect('agrodata.db')
    cursor = conn.cursor()

    cursor.execute('SELECT PID , PNAME , PDETAILS , QUANTITY , PRICE , CATEGORY , IMG FROM cart WHERE cid=?', ( cid ))
    item = cursor.fetchone()

    if not item:
        return redirect(url_for('routes.cart'))
    
    cursor.execute("""
        INSERT INTO orders (PID, PNAME, PDETAILS, QUANTITY, PRICE, CATEGORY, IMG)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, item)

    cursor.execute("DELETE FROM cart WHERE cid=?", (cid))
    conn.commit()
    conn.close()
    
    return redirect(url_for('routes.cart'))


@routes.route('/orders')
def orders():
    if 'username' not in session:
        return redirect(url_for('routes.login'))
    conn = sqlite3.connect('agrodata.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM orders')
    orders = cursor.fetchall()
    
    conn.close()
    
    
    return render_template('orders.html',orders=orders)



@routes.route('/payment')
def payment():
    if 'username' not in session:
        return redirect(url_for('routes.login'))
    username = session['username']
    return render_template('payment.html', username=username)

@routes.route('/receipts')
def receipts():
    return render_template('receipts.html')

@routes.route('/seller')
def seller():
    return render_template('seller.html')

@routes.route('/help')
def help():
    return render_template('help.html')

@routes.route('/profile/update', methods=['GET', 'POST'])
def update_profile():
    if 'username' not in session:
        return redirect(url_for('routes.login'))
    
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']
        state = request.form['state']
        zip_code = request.form['zip']
        
        username = session['username']
        
        conn = sqlite3.connect('agrodata.db')
        cursor = conn.cursor()
        cursor.execute('''
                    UPDATE users 
                    SET name=?, city=?, state=?, zip=? 
                    WHERE username=?''', (name, city, state, zip_code, username))
        conn.commit()
        conn.close()
        
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('routes.profile'))

@routes.route('/profile/update/password', methods=['GET', 'POST'])
def update_password():
    if 'username' not in session:
        return redirect(url_for('routes.login'))
    
    if request.method == 'POST':
        new_password = request.form['new_password']
        username = session['username']
        conn = sqlite3.connect('agrodata.db')
        cursor = conn.cursor()
        cursor.execute('''UPDATE users Set password=? WHERE username=?''', (new_password, username))
        conn.commit()
        conn.close()
        flash('Password updated successfully!', 'success')
        return redirect(url_for('routes.login'))

    
