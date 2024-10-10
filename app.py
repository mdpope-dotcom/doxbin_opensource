from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Import admin routes
import admin  # Make sure this import is at the bottom of your app.py

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add_paste', methods=['GET', 'POST'])
def add_paste():
    if request.method == 'POST':
        # Logic to save the paste goes here
        return redirect(url_for('index'))
    return render_template('add_paste.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Logic to authenticate user goes here
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Logic to register user goes here
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/tos')
def tos():
    return render_template('tos.html')

@app.route('/telegram')
def telegram():
    return render_template('telegram.html')

if __name__ == '__main__':
    app.run(debug=True)
