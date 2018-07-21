""" Gets the correct Model for the application """
#model_version = 'Dictionary'
model_version = 'SQL'

def get_model():
	if model_version == 'Dictionary':
		from .model_pydict import model
	elif model_version == 'SQL':
		from .model_sqlite3 import model
	else:
		raise ValueError("No database version selected.")
	return model()
