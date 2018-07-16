""" This is a Movie Review flask application """
from flask import Flask, redirect, request, url_for, render_template
import MRModels

app = Flask(__name__)
model = MRModels.get_model()

""" Function decorator using app.route ( '/', index() ) """
@app.route('/')
@app.route('/index.html')
def index():
    """ Main movie review webpage """
    return render_template('index.html')

@app.route('/reviews')
def reviews():
    """ Displays all the movie reviews within a webpage """
    reviews = model.select()
    return render_template('reviews.html', reviews=reviews)

if __name__ == '__main__':
    app.run(port=8000, debug=True)
