""" Python datastore model. """
from flask import current_app
from google.appengine.datastore.datastore_query import Cursor
from google.appengine.ext import ndb

builtin_list = list

def init_app(app):
    """ Initializes the moviereviews Datastore model. """
    pass

class MovieReview(ndb.Model):
    """ Creates the MovieReview Datastore Kind (table) and then sets the entity properties (attributes). """
    movie = ndb.StringProperty()
    year = ndb.IntegerProperty()
    genre = ndb.StringProperty()
    rating = ndb.IntegerProperty()
    review = ndb.StringProperty()
    reviewer = ndb.StringProperty()

def from_datastore(entity):
    """ Returns the Datastore moviereview entity in the form {id: id, prop: val, ...}, as required by the application. """
    if not entity:
        return None
    if isinstance(entity, builtin_list):
        entity = entity.pop()

    moviereview = {}
    moviereview['id'] = entity.key.id()
    moviereview['movie'] = entity.movie
    moviereview['year'] = entity.year
    moviereview['genre'] = entity.genre
    moviereview['rating'] = entity.rating
    moviereview['review'] = entity.review
    moviereview['reviewer'] = entity.reviewer
    return moviereview

def list(limit=10, cursor=None):
    """ Returns the moviereview entities from the DataStore converted to a list (limit 10 per list), with each entry containing
        the movie id, title, year, genre, rating, review and reviewer. """
    if cursor:
        cursor = Cursor(urlsafe=cursor)

    query = MovieReview.query().order(MovieReview.movie)
    entities, cursor, more = query.fetch_page(limit, start_cursor=cursor)
    entities = builtin_list(map(from_datastore, entities))
    return entities, cursor.urlsafe() if len(entities) == (limit + 1) else None

def read(id):
    """ Takes a moviereview key and returns the corresponding entity (movie id, title, year, genre, rating, 
    review and reviewer) from the DataStore. """
    
    moviereview_key = ndb.Key('MovieReview', int(id))
    results = moviereview_key.get()
    return from_datastore(results)

def update(data, id=None):
    """ Takes a moviereview key and updates or creates the corresponding entity (movie id, title, year, genre, rating, 
    review and reviewer) in the DataStore. """
    if id:
        key = ndb.Key('MovieReview', int(id))
        moviereview = key.get()
    else:
        moviereview = MovieReview()

    moviereview.movie = data['movie']
    moviereview.year = int(data['year'])
    moviereview.genre = data['genre']
    moviereview.rating = int(data['rating'])
    moviereview.review = data['review']
    moviereview.reviewer = data['reviewer']
    moviereview.put()
    return from_datastore(moviereview)

create = update

def delete(id):
    """ Takes a moviereview key and deletes the corresponding entity (movie id, title, year, genre, rating, 
    review and reviewer) from the DataStore. """
    key = ndb.Key('MovieReview', int(id))
    key.delete()
