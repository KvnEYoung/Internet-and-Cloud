#!/usr/bin/env python3
# Copyright (c) 2018 Jeff Lund, Kevin Young
'''
Movie review flask app
'''

from flask import Flask, redirect, request, url_for, render_template, current_app, Blueprint
from Reviews import get_model
from .talktome import read_text

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@views.route('/index', methods=['GET', 'POST'])
def index():
  """"
  Renders landing page for movie review site.
  POST request changes language setting
  """
  model = get_model()
  pageText = ['Welcome to Ripe Tomatoes', 'A fresher movie review site', 'Please select the review language',
  	'English', 'Spanish', 'Italian', 'Submit', 'Current language is', 'Movie Reviews', 'Add Movie Reviews']
  pageTranslation = model.translate_list(pageText)

  if request.method == 'POST':
     lang = request.form['review_lang']
     current_app.config.update(LANGUAGE=lang)
     return redirect(url_for('views.index'))

  return render_template('index.html', language=full_language(), text=pageTranslation)


@views.route('/reviews', methods=['GET', 'POST'])
def reviews():
  """
  Renders all reviews from the model.
  """
  # Databases returned in tuple (Movie, Review)
  # Must be unpacked before use in render template.
  model = get_model()
  dbs = model.select()
  if dbs is None:
      dbs = [[],[]]
  movies = dbs[0]
  reviews = dbs[1]
  if request.method == 'POST':
      text = 'placeholder'
      id = int(request.form['synth'])
      # Find text associated with review id - super ugly
      for row in reviews.values():
          for list_element in row:
              if id == list_element['id']:
                  text = list_element['review']
      stream = read_text(text)
      return redirect(url_for('views.synth', stream=stream))

  pageText = ['Movie Reviews!', 'Main Page', 'Add Movie Review', 'Directed By', 'Released', 'Rating', 'Runtime',
  	'Genre', 'Talk to me', 'Rating', 'Author']
  pageTranslation = model.translate_list(pageText)

  return render_template('reviews.html', movies=movies, reviews=reviews, text=pageTranslation)

@views.route('/submit', methods=['GET', 'POST'])
def submit():
  """
  Renders submission form to submit a new movie review.
  """
  model = get_model()
  pageText = ['Name of Movie', 'Released', 'Year', 'Director', 'Movie Rated', 'Not Rated',
  	'Runtime', 'minutes', 'Genres', "Write your review here", 'Rating', 'Reviewed by',
  	'Submit Review', 'Main Page']

  # Defines available genres for the a movie. Makes list available in GET and POST.
  genres = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', \
    'Documentary', 'Drama', 'Family', 'Fantasy', 'Film Noir', 'History', 'Horror', \
    'Indie','Music', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Short', 'Sport', \
    'Superhero', 'Thiller', 'War', 'Western']

  pageTranslation = model.translate_list(pageText)
  genresTranslation = model.translate_list(genres)

  if request.method == 'POST':
    genre_selected = [gen for gen in genres if gen in request.form]
    model.insert(request.form['mov_name'], request.form['release_year'], \
      request.form['director'], request.form['mov_rating'], \
      request.form['runtime'], ','.join(genre_selected), request.form['review'], \
      request.form['rev_name'], request.form['rev_rating'])

    return redirect(url_for('views.reviews'))

  return render_template('submit.html', genres=genresTranslation, text=pageTranslation)

@views.route('/synth/<filename>')
def synth(filename):
    # get id file
    gcs_file = gcs.open(filename)
    audio = gcs_file.read()
    gcs_file.close()
    textTranslation = model.translate_text('Your browser does not support the audio element.')
    return render_template('synth.html', audio=audio, static_text=textTranslation)

def full_language():
  model = get_model()
  language = {'en': 'English', 'es': 'Spanish', 'it' : 'Italian'}
  return  model.translate_text(language[current_app.config['LANGUAGE']])
