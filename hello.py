
# hello.py
import os

from flask import Flask, request, render_template, url_for, redirect, flash
app = Flask(__name__)

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == "POST":
        if valid_login(request.form['username'], request.form['password']):
            flash("successfully logged in")
            return redirect(url_for('welcome', username=request.form.get('username')))
        else:
            error = "Incorrect username and password"

    return render_template('login.html', error=error)


def valid_login(username, password):
    if (username == password) and username:
        flash("valid_login")
        return True
    else:
        return False

@app.route('/welcome/<username>')
def welcome(username):
    return render_template('welcome.html', username=username)

if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.secret_key = 'this is a secret key'
    app.run(host=host, port=port, debug=True)
