from flask import Flask, render_template, request, redirect, url_for, session
import uuid

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

# In-memory storage for pastes and admin status
pastes = {}

@app.route('/')
def index():
    return render_template('index.html', pastes=pastes)

@app.route('/paste/new', methods=['GET', 'POST'])
def new_paste():
    if request.method == 'POST':
        title = request.form['pasteTitle']
        content = request.form['pasteContent']
        paste_id = str(uuid.uuid4())
        pastes[paste_id] = {'title': title, 'content': content}
        return redirect(url_for('view_paste', paste_id=paste_id))
    return render_template('new_paste.html')

@app.route('/paste/<paste_id>')
def view_paste(paste_id):
    paste = pastes.get(paste_id)
    if paste:
        return render_template('view_paste.html', title=paste['title'], content=paste['content'])
    return "Paste not found.", 404

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'password':
            session['logged_in'] = True
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
