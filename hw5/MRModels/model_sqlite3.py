""" Python database model. """
from .Model import Model
import sqlite3
database = 'reviews.db'    # Database file for selections/insertions

class model(Model):
    def __init__(self):
        """ Verifying if the reviews table exists within the database and if not creates it. """
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from reviews")
        except sqlite3.OperationalError:
            cursor.execute("create table reviews (movie text, year integer, genre text, rating integer, review text, reviewer text)")
        cursor.close()

    def select(self):
        """ Returns all the database reviews converted to a list for the html webpage, with each row containing
        the movie title, year, genre, rating, review and reviewer. """
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM reviews")
        return cursor.fetchall()

    def insert(self, movie, year, genre, rating, review, reviewer):
        """ Inserts movie reviews (title, year, genre, rating, review and reviewer) into the database reviews table. """
        values = {'movie':movie, 'year':year, 'genre':genre, 'rating':rating, 'review':review, 'reviewer':reviewer}
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute("insert into reviews (movie, year, genre, rating, review, reviewer) VALUES (:movie, :year, :genre, :rating, :review, :reviewer)", values)
        connection.commit()
        cursor.close()
        return True