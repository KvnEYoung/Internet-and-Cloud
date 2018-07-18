""" Gets the correct Model for the application """

def get_model():
	from .model_sqlite3 import model
	return model()
