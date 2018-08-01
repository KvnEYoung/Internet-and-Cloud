from flask import current_app, Flask, redirect, url_for
#Flask app factory to initialize Movie Review app.
def create_app():
    '''
    Creates and configures a new app 
    '''
    app = Flask(__name__)
    with app.app_context():
        model = get_model()

    from .pages import pages
    app.register_blueprint(pages)

    @app.route('/')
    def index():
        return redirect(url_for('pages.index'))

    return app

def get_model():
    '''
    Imports and returns the datastore model
    '''
    from . import model_datastore
    model = model_datastore
    return model
