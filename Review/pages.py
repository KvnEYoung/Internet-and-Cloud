from flask import Blueprint, redirect, render_template, request, url_for
from Review import get_model

pages = Blueprint('pages', __name__)

@pages.route('/index')
def index():
    '''
    Renders the landing page
    '''
    return render_template('index.html')

@pages.route('/reviews')
def reviews():
    '''
    Renders all reviews from the model.
    '''
    model = get_model()
    #databases must be unpacked before use in render template.
    dbs = model.select()
    return render_template('reviews.html', movies=dbs[0], reviews=dbs[1])

@pages.route('/submit', methods=['GET', 'POST'])
def submit():
    '''
    On GET renders a page to submit a new review.
    On POST form information is inserted into the model and redirects to the reviews page.
    '''
    genres = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy',
        'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'Film Noir',
        'History', 'Horror', 'Indie','Music', 'Musical', 'Mystery', 'Romance',
        'Sci-Fi', 'Short', 'Sport', 'Superhero', 'Thiller', 'War', 'Western']

    if request.method == 'POST':
        model = get_model()
        genre_selected = [g for g in genres if g in request.form]
        model.insert(request.form['mov_name'], request.form['release_year'],
            request.form['director'], request.form['mov_rating'],
            request.form['runtime'], ','.join(genre_selected), request.form['review'],
            request.form['rev_name'], request.form['rev_rating'])
        return redirect(url_for('pages.reviews'))
    return render_template('submit.html', genres=genres)
