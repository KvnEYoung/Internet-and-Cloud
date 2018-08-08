from flask import render_template
from flask.views import MethodView
import movie_models as mm

class reviews(MethodView):
    def get(self):
        """
        Renders all reviews from the model.
        """
        model = mm.get_model()
        #databases must be unpacked before use in render template.
        dbs = model.select()
        return render_template('reviews.html', movies=dbs[0], reviews=dbs[1])
