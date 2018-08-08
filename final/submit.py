from flask import render_template, redirect, url_for, request
from flask.views import MethodView
import movie_models as mm

class submit(MethodView):
    def __init__(self):
        """
        Defines available genres for the a movie. Makes list available in GET and POST.
        """
        self.genres = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy',
        'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'Film Noir',
        'History', 'Horror', 'Indie','Music', 'Musical', 'Mystery', 'Romance',
         'Sci-Fi', 'Short', 'Sport', 'Superhero', 'Thiller', 'War', 'Western']

    def get(self):
        """
        Renders submission form to submit a new movie review.
        """
        return render_template('submit.html', genres = self.genres)

    def post(self):
        """
        POST request to process form data to insert new review into model.
        Redirect to reviews page after submission.
        """
        model = mm.get_model()
        genre_selected = [g for g in self.genres if g in request.form]
        model.insert(request.form['mov_name'], request.form['release_year'],
        request.form['director'], request.form['mov_rating'],
        request.form['runtime'], ','.join(genre_selected), request.form['review'],
        request.form['rev_name'], request.form['rev_rating'])
        return redirect(url_for('reviews'))
