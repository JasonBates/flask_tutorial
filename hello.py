
# hello.py
import os

from flask import Flask, request, render_template, url_for
app = Flask(__name__)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        return "User %s has logged in" % request.form['username']
    else:
        return render_template('login.html')

if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.run(host=host, port=port, debug=True)
