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
    reviews = [dict(movie=row[0], year=row[1], genre=row[2], rating=row[3], review=row[4], reviewer=row[5]) for row in model.select()]
    return render_template('reviews.html', reviews=reviews)

@app.route('/newreview', methods=['GET','POST'])
def newreview():
    """ Webpage to add a new movie review """
    #model.insert(request.form['movie'], request.form['year'], request.form['genre'],
    #request.form['rating'], request.form['review'], request.form['reviewer'])
    return render_template('newreview.html')

if __name__ == '__main__':
    app.run(port=8000, debug=True)
