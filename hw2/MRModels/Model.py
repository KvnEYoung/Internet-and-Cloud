class Model():
    def __init__(self):
        self.moviereviews = {}
        self.insert()

    def select(self):
        return self.moviereviews

    def insert(self):
        self.moviereviews["movie1"] = { "movie":"The Purge", "year":2013, "genre":"Horror", "rating":3,"review":"Horrible", "reviewer": "John Doe"}
        self.moviereviews["movie2"] = { "movie":"Star Wars", "year":1978, "genre":"Sci-Fi", "rating":10,"review":"Excellent", "reviewer": "Johnny Doe"}
        self.moviereviews["movie3"] = { "movie":"Avengers", "year":2012, "genre":"Sci-Fi", "rating":9,"review":"Very good", "reviewer": "Jane Doe"}
        self.moviereviews["movie4"] = { "movie":"Deadpool", "year":2016, "genre":"Sci-Fi", "rating":9,"review":"Great movie", "reviewer": "Jimmy Doe"}
        self.moviereviews["movie5"] = { "movie":"Harry Potter and the Sorcerer's Stone", "year":2001, "genre":"Fantasy", "rating":10,"review":"Fantastic", "reviewer": "Jonathan Doe"}
        self.moviereviews["movie6"] = { "movie":"Pitch Perfect", "year":2012, "genre":"Comedy", "rating":8,"review":"Funny movie", "reviewer": "Ginger Doe"}
        pass
