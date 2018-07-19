""" Python database model """
from .Model import Model
import sqlite3
DB_FILE = 'reviews.db'    # file for our Database

class model(Model):
    def __init__(self):
        # Make sure our database exists
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from reviews")
        except sqlite3.OperationalError:
            cursor.execute("create table reviews (movie text, year integer, genre text, rating integer, review text, reviewer text)")
        cursor.close()

    def select(self):
        """
        Gets all rows from the database
        Each row contains: name, email, date, message
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM reviews")
        return cursor.fetchall()

    def insert(self, movie, year, genre, rating, review, reviewer):
        values = {'movie':movie, 'year':year, 'genre':genre, 'rating':rating,
        'review':review, 'reviewer':reviewer}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into reviews (movie, year, genre, rating, review, reviewer) VALUES (:movie, :year, :genre, :rating, :review, :reviewer)", values)

        connection.commit()
        cursor.close()
        return True