LANGUAGE = 'en'
PROJECT_ID = 'lund-young-510'
DATA_BACKEND = 'datastore'
SECRET_KEY = 'banana'

# uncomment if using cloudsql
#DATA_BACKEND='cloudsql'
#CLOUDSQL_USER='root'
#CLOUDSQL_PASSWORD = 'cs510'
#CLOUDSQL_DATABASE = 'movie-reviews'
#CLOUDSQL_CONNECTION_NAME = 'lund-young-510:us-west1:movie-reviews'
#LIVE_SQLALCHEMY_DATABASE_URI = (
#    'mysql+pymysql://{user}:{password}@localhost/{database}'
#    '?unix_socket=/cloudsql/{connection_name}').format(
#        user=CLOUDSQL_USER, password=CLOUDSQL_PASSWORD,
#        database=CLOUDSQL_DATABASE, connection_name=CLOUDSQL_CONNECTION_NAME)
