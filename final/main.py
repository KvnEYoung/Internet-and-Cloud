#!/usr/bin/env python3
# Copyright (c) 2018 Jeff Lund
'''
Movie review flask app
'''

from flask import Flask, url_for, render_template
from flask.views import MethodView
from index import index
from reviews import reviews
from submit import submit

app = Flask(__name__)

app.add_url_rule('/', view_func=index.as_view('index'), methods=['GET', 'POST'])
app.add_url_rule('/reviews', view_func=reviews.as_view('reviews'), methods=['GET'])
app.add_url_rule('/submit', view_func=submit.as_view('submit'), methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
