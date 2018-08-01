from flask import current_app
from google.appengine.ext import ndb

# Start Model
class Movie(ndb.Model):
    '''
    Model to hold static details for a given movie
    :param mov_name: Name of the movie
    :param director: Director
    :param mov_rating: MPAA rating (i.e G, PG-13, R, etc)
    :param runtime: Runtime in minutes
    :param genre: Genre categories for a movie. Multiple genres are allowed. Stored in a single string
        with each value seperated by a comma
    '''
    mov_name = ndb.StringProperty()
    release_year = ndb.IntegerProperty()
    director = ndb.StringProperty()
    mov_rating = ndb.StringProperty()
    runtime = ndb.IntegerProperty()
    genre = ndb.StringProperty()

class Reviews(ndb.Model):
    '''
    Model to hold reviews. mov_name acts as a key to associate each entry with Movie model
    :param mov_name: Name of the movie
    :param review: Text of the review
    :param rev_name: Reviewers Name
    :param rev_rating: Reviewers rating, 1-5
    '''
    mov_name = ndb.StringProperty()
    review = ndb.TextProperty()
    rev_name = ndb.StringProperty()
    rev_rating = ndb.IntegerProperty()
# End Model

def select():
    '''
    Retrieves information from models for Movies and Reviews. Queries are transformed into 
    2-dimensional dictionaries with the movie's name as the key.
    :return List of dictionaries. Movies in index 0, Reviews in index 1
    '''
    query_movie = Movie.query().order(Movie.mov_name).fetch()
    query_reviews = Reviews.query().order(Reviews.mov_name).fetch()
    movies = { m.mov_name: {
                            'release_year': m.release_year,
                            'director': m.director,
                            'mov_rating': m.mov_rating,
                            'runtime': m.runtime,
                            'genre': m.genre.split(',') }
                            for m in query_movie }
    reviews = { r.mov_name: [] for r in query_reviews }
    for row in query_reviews:
        reviews[row.mov_name].append({
                                'review':row.review,
                                'rev_name':row.rev_name,
                                'rev_rating':row.rev_rating })
    return [movies, reviews]


def insert(mov_name, release_year, director, mov_rating,
            runtime, genre, review, rev_name, rev_rating):
    '''
    Inserts a new review into Review model. If it is the first review for a given movie
    then a new entry is first created in the Movie model.

    '''
    if Movie.query(Movie.mov_name==mov_name).get() is None:
        Movie(mov_name=mov_name, release_year=int(release_year), director=director,
            mov_rating=mov_rating, runtime=int(runtime), genre=genre).put()
    
    Reviews(mov_name=mov_name, review=review, rev_name=rev_name,
        rev_rating=int(rev_rating)).put()
