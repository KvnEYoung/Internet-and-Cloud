#sqlite model
import sqlite3 as sl3
from .Model import Model

MOVIES_DB = 'movies.db'
REVIEWS_DB = 'reviews.db'


class model(Model):
    def __init__(self):
        """"
        :param movies: contains fixed details about for a movie
        :param reviews: contains reviews and review metadata for each movie
        """
        mconn = sl3.connect(MOVIES_DB)
        mcursor = mconn.cursor()
        rconn = sl3.connect(REVIEWS_DB)
        rcursor = rconn.cursor()
        mcursor.execute(
            'CREATE TABLE IF NOT EXISTS movies ( \
            mov_name TEXT UNIQUE, \
            release_year INTEGER, \
            director TEXT, \
            mov_rating TEXT, \
            runtime INTEGER, \
            genre TEXT)')
        rcursor.execute(
            'CREATE TABLE IF NOT EXISTS reviews (\
            mov_name TEXT, \
            review TEXT, \
            rev_name TEXT, \
            rev_rating INTEGER \
        )')
        mcursor.close()
        rcursor.close()
        
        self.language = "en"


    def select(self):
        """
        Retrieves information from movies and reviews databases. Inserts both into
        dictionaries using the movie's name as the keyself.
        :return List of dictionaries. Movies database in index 0, review database in index 1self.
        """
        mconn = sl3.connect(MOVIES_DB)
        mconn.row_factory = sl3.Row
        mcursor = mconn.cursor()
        movies_sql = mcursor.execute('SELECT * FROM movies').fetchall()
        mcursor.close()
        movies = { m['mov_name']: {
                                'release_year': m['release_year'],
                                'director': m['director'],
                                'mov_rating': m['mov_rating'],
                                'runtime': m['runtime'],
                                'genre': m['genre'].split(',') }
                                for m in movies_sql }

        rconn = sl3.connect(REVIEWS_DB)
        rconn.row_factory = sl3.Row
        rcursor = rconn.cursor()
        reviews_sql = rcursor.execute('SELECT * FROM reviews').fetchall()
        rcursor.close()
        reviews = { r['mov_name']: [] for r in reviews_sql }
        for row in reviews_sql:
            reviews[row['mov_name']].append({
                                    'review':row['review'],
                                    'rev_name':row['rev_name'],
                                    'rev_rating':row['rev_rating'] })
        return [movies, reviews]

    def insert(self, mov_name, release_year, director, mov_rating,
				runtime, genre, review, rev_name, rev_rating):
        """
        Inserts a new review into databases. If it is the first revew for a movies
        then a new entry is created in movies databse. Otherwise only review information
        is inserted.
        """
        conn = sl3.connect(MOVIES_DB)
        cursor = conn.cursor()
        if cursor.execute('SELECT * FROM movies WHERE mov_name = ?', (mov_name,)).fetchone() == None:
            cursor.execute('INSERT INTO movies (mov_name, release_year, director, mov_rating, runtime, genre) \
                VALUES (?, ?, ?, ?, ?, ?)', (mov_name, release_year, director, mov_rating, runtime, genre,))
        conn.commit()
        cursor.close()

        conn = sl3.connect(REVIEWS_DB)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO  reviews (mov_name, review, rev_name, rev_rating) \
            VALUES (?, ?, ?, ?)', (mov_name, review, rev_name, rev_rating,))
        conn.commit()
        cursor.close()
        
def translate_text(text):
  translate_client = translate.Client()
  language = current_app.config['LANGUAGE']

  if isinstance(text, six.binary_type):
    text = text.decode('utf-8')

  result = translate_client.translate(text, target_language=language)
  return result['translatedText']

def translate_list(list):

	list = [translate_text(item) for item in list]
	return list
