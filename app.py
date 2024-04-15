from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world"


@app.route('/hel')
def hel():
    return 'Helllll'

@app.route('/test')
def test():
    data = request.args.get('x')
    return 'this is the op {}'.format(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0')