#!/usr/bin/env python3
# Copyright (c) 2018 Jeff Lund, Kevin Young
'''
Movie review flask app
'''

from flask import Flask, redirect, request, url_for, render_template
import movie_models as mm

app = Flask(__name__)
model = mm.get_model()

""" Function decorator using app.route ( '/', index() ). """
@app.route('/')
@app.route('/index.html', methods=['GET', 'POST'])
def index():
    """Renders landing page for movie review site. """
    if request.method == 'GET':
        language = model.getLanguage()
        return render_template('index.html', language=language)
		
    else:
        """ POST request to process form data to change the language of reviews. """
        model.setLanguage(request.form['review_lang'])
        language = model.getLanguage()
        return render_template('index.html', language=language)

        
@app.route('/reviews')
def reviews():
    """ Renders all reviews from the model. """
    #databases must be unpacked before use in render template.
    dbs = model.select()
    return render_template('reviews.html', movies=dbs[0], reviews=dbs[1])

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    """ Defines available genres for the a movie. Makes list available in GET and POST. """
	
    genres = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy',
        'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'Film Noir',
        'History', 'Horror', 'Indie','Music', 'Musical', 'Mystery', 'Romance',
        'Sci-Fi', 'Short', 'Sport', 'Superhero', 'Thiller', 'War', 'Western']
         
    if request.method == 'GET':
        """ Renders submission form to submit a new movie review. """
        return render_template('submit.html', genres=genres)

    else:
        """ POST request to process form data to insert new review into model.
        Redirect to reviews page after submission. """
        genre_selected = [g for g in genres if g in request.form]
        model.insert(request.form['mov_name'], request.form['release_year'],
        request.form['director'], request.form['mov_rating'],
        request.form['runtime'], ','.join(genre_selected), request.form['review'],
        request.form['rev_name'], request.form['rev_rating'])
        return redirect(url_for('reviews'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
