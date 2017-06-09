from .models import User
from flask import

app = flask(__name__)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if len(username) < 1:
            flash('Your username must be at least one character.')
        elif len(password) < 5:
            flash('Your password must be longer than 5 characters.')
        elif not User(username).register(password):
            flash('Username already exists!')
        else:
            session['username'] = username
            flash['signed in']
            return redirect(url_for('index'))

    return render_template('register.html')

@app.route("/signin", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not User(username).verify_password(password):
            flash('Invalid Signin')
        else:
            session['username'] = username
            flash("Signed In")
            return redirect(url_for('index'))

    return render_template('login.html')

