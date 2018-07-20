""" Gets the correct Model for the application """

def get_model():
	from .model_pydict import model
	return model()
