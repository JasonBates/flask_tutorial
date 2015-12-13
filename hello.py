
# hello.py
import os

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    import pdb; pdb.set_trace()
    i = 3
    i = i +1
    visited = i
    return "Hello everyone and you!" + str(visited)

if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.run(host=host, port=port, debug=True)
