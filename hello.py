
# hello.py
import os

from flask import Flask, request
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return request.values['username']
    return '<form method="POST" action="/login"> \
            <input type="text" name="username" /> \
            <p><button type="submit">submit</button> \
            </form>'

if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.run(host=host, port=port, debug=True)
