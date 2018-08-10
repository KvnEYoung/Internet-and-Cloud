#cloud_sql model
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, current_app

db = SQLAlchemy()

def init_app(app):
  app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', False)
  db.init_app(app)

class Movies(db.Model):
  '''
  Model to hold static details for a given movie
  :param mov_name: Name of the movie
  :param director: Director
  :param mov_rating: MPAA rating (i.e G, PG-13, R, etc)
  :param runtime: Runtime in minutes
  :param genre: Genre categories for a movie. Multiple genres are allowed. Stored in a single string
  with each value seperated by a comma
  '''
  __tablename__ = 'movies'
  mov_name = db.Column(db.String(255), primary_key=True)
  release_year = db.Column(db.Integer())
  director = db.Column(db.String(255))
  mov_rating = db.Column(db.String(255))
  runtime = db.Column(db.Integer())
  genre = db.Column(db.String(255))

class Reviews(db.Model):
  '''
  Model to hold reviews. mov_name acts as a key to associate each entry with Movie model
  :param mov_name: Name of the movie
  :param review: Text of the review
  :param rev_name: Reviewers Name
  :param rev_rating: Reviewers rating, 1-5
  '''
  __tablename = 'reviews'
  mov_name = db.Column(db.String(255), primary_key=True)
  review = db.Column(db.Text())
  rev_name = db.Column(db.String(255))
  rev_rating = db.Column(db.Integer())

def select():
  """
  Retrieves information from movies and reviews databases. Inserts both into
  dictionaries using the movie's name as the keyself.
  :return List of dictionaries. Movies database in index 0, review database in index 1self.
  """
  movies_query = Movies.query().all()
  movies = { m['mov_name']: {
    'release_year': m['release_year'],
    'director': m['director'],
    'mov_rating': m['mov_rating'],
    'runtime': m['runtime'],
    'genre': m['genre'].split(',') }
    for m in movies_query }

  review_query = Reviews.query().all()
  reviews = { r['mov_name']: [] for r in reviews_query }
  for row in reviews_query:
    reviews[row['mov_name']].append({
      'review':row['review'],
      'rev_name':row['rev_name'],
      'rev_rating':row['rev_rating'] })
    return [movies, reviews]

def insert(mov_name, release_year, director, mov_rating,
		runtime, genre, review, rev_name, rev_rating):
  """
  Inserts a new review into databases. If it is the first revew for a movies
  then a new entry is created in movies databse. Otherwise only review information
  is inserted.
  """
  if Movies.query().filter_by(mov_name=mov_name).first() is None:
    data = Movies(mov_name, release_year, director, mov_rating,
      runtime, ','.join(genre))
    db.session.add(data)
    db.session.commit()

  data = Reviews(mov_name, review, rev_name, rev_rating)
  db.session.add(data)
  db.session.commit()

def setLanguage(review_lang):
  current_app.config['LANGUAGE'] = review_lang

def getLanguage():
  return current_app.config['LANUAGE']
