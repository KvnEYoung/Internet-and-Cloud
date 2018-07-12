from flask import flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index'

if __name__ = '__main__':
    app.run(debug=true)
