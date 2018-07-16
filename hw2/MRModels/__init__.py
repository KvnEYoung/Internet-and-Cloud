""" Gets the correct Model for the application """

def get_model():
	from .Model import Model
	return Model()
