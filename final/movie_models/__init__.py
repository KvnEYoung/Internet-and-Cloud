backend = 'sqlite'

def get_model():
    if backend == 'sqlite':
    	from .model_sql import model
    else:
        raise ValueError("Invalid backend configuration")
    return model()
