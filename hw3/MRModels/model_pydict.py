""" Python dictionary model """
from .Model import Model

class model(Model):
    def __init__(self):
        """ Initializes the moviereviews dictionary and then adds the hardcoded movie reviews """
        self.moviereviews = {}
        self.moviereviews["movie0"] = { "movie":"The Purge", "year":2013, "genre":"Horror", "rating":3,"review":"Horrible", "reviewer": "John Doe"}
        self.moviereviews["movie1"] = { "movie":"Star Wars", "year":1978, "genre":"Sci-Fi", "rating":10,"review":"Excellent", "reviewer": "Johnny Doe"}
        self.moviereviews["movie2"] = { "movie":"Avengers", "year":2012, "genre":"Sci-Fi", "rating":9,"review":"Very good", "reviewer": "Jane Doe"}
        self.moviereviews["movie3"] = { "movie":"Deadpool", "year":2016, "genre":"Sci-Fi", "rating":9,"review":"Great movie", "reviewer": "Jimmy Doe"}
        self.moviereviews["movie4"] = { "movie":"Harry Potter and the Sorcerer's Stone", "year":2001, "genre":"Fantasy", "rating":10,"review":"Fantastic", "reviewer": "Jonathan Doe"}
        self.moviereviews["movie5"] = { "movie":"Pitch Perfect", "year":2012, "genre":"Comedy", "rating":8,"review":"Funny movie", "reviewer": "Ginger Doe"}

    def select(self):
        """ Returns all the moviereviews dictionary entries, with each entry containing
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