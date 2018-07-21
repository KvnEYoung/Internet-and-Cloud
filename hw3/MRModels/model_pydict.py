""" Python dictionary model """
from .Model import Model

class model(Model):
    def __init__(self):
        """ Initializes the moviereviews dictionary and then adds the hardcoded movie reviews """
        self.moviereviews = {}
        self.insert("The Purge", 2013, "Horror", 3, "Horrible", "John Doe")
        self.insert("Star Wars", 1978, "Sci-Fi", 10, "Excellent", "Johnny Doe")
        self.insert("Avengers", 2012, "Sci-Fi", 9, "Very good", "Jane Doe")
        self.insert("Deadpool", 2016, "Sci-Fi", 9, "Great movie", "Jimmy Doe")
        self.insert("Harry Potter and the Sorcerer's Stone", 2001, "Fantasy", 10, "Fantastic", "Jonathan Doe")
        self.insert("Pitch Perfect", 2012, "Comedy", 8, "Funny movie", "Ginger Doe")

    def select(self):
        """ Returns all the moviereviews dictionary entries converted to a list for the html webpage, with each entry containing
        the movie title, year, genre, rating, review and reviewer """
        templist = []
        for key in self.moviereviews.keys():
            review = self.moviereviews[key]
            tempreview = (review['movie'], review['year'], review['genre'], review['rating'], review['review'], review['reviewer'])
            templist.append(tempreview)
        return templist

    def insert(self, movie, year, genre, rating, review, reviewer):
        """ Inserts movie reviews (title, year, genre, rating, review and reviewer) into the moviereview dictionary """
        movienumber = "movie" + str(len(self.moviereviews.keys()))
        self.moviereviews[movienumber] = { "movie":movie, "year":year, "genre":genre, "rating":rating, "review":review, "reviewer":reviewer}
        return True