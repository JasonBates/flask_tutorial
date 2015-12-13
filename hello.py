
# hello.py
import os

from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def hello_world():
    return "Hello everyone and you!"

@app.route('/user/<username>')
def show_user_profile(username):
    print(username)
    return "User %s" % username

@app.route('/userno/<int:userno>')
def show_user_num(userno):
    return "User %d " % userno


if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.run(host=host, port=port, debug=True)
