from flask import render_template
from flask.views import MethodView
import movie_models as mm

class index(MethodView):
    def get(self):
        """
        Renders landing page for movie review site.
        """
        return render_template('index.html')
