# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask import current_app
from google.appengine.datastore.datastore_query import Cursor
from google.appengine.ext import ndb


builtin_list = list


def init_app(app):
    pass


# [START model]
class Book(ndb.Model):
    movie = ndb.StringProperty()
    year = ndb.IntegerProperty()
    genre = ndb.StringProperty()
    rating = ndb.IntegerProperty()
    review = ndb.StringProperty()
    reviewer = ndb.StringProperty()
# [END model]


# [START from_datastore]
def from_datastore(entity):
    """Translates Datastore results into the format expected by the
    application.

    Datastore typically returns:
        [Entity{key: (kind, id), prop: val, ...}]

    This returns:
        {id: id, prop: val, ...}
    """
    if not entity:
        return None
    if isinstance(entity, builtin_list):
        entity = entity.pop()
        book = {}
        book['id'] = entity.key.id()
        book['movie'] = entity.movie
        book['year'] = entity.year
        book['genre'] = entity.genre
        book['rating'] = entity.rating
        book['review'] = entity.review
        book['reviewer'] = entity.reviewer
    return book
# [END from_datastore]



# [START list]
def list(limit=10, cursor=None):
    if cursor:
        cursor = Cursor(urlsafe=cursor)
        query = Book.query().order(Book.movie)
        entities, cursor, more = query.fetch_page(limit, start_cursor=cursor)
        entities = builtin_list(map(from_datastore, entities))
    return entities, cursor.urlsafe() if len(entities) == limit else None
# [END list]


# [START read]
def read(id):
    book_key = ndb.Key('Book', int(id))
    results = book_key.get()
    return from_datastore(results)
# [END read]


# [START update]
def update(data, id=None):
    if id:
        key = ndb.Key('Book', int(id))
        book = key.get()
    else:
        book = Book()
        book.movie = data['movie']
        book.year = data['year']
        book.genre = data['genre']
        book.rating = data['rating']
        book.review = data['review']
        book.reviewer = data['reviewer']
        book.put()
    return from_datastore(book)

create = update
# [END update]


# [START delete]
def delete(id):
    key = ndb.Key('Book', int(id))
    key.delete()
# [END delete]

