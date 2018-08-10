#backend = 'sqlite'
backend = 'cloudsql'
def get_model():
    if backend == 'sqlite':
        from .model_sql import model
    else if:
        backend == 'cloudsql':
        from .model_cloudsql import model
    else:
        raise ValueError("Invalid backend configuration")
    return model()
