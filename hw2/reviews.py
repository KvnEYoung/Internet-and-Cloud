from flask import render_template
from flask.views import MethodView

class Reviews(MethodView):
    def get(self):
        return render_template('reviews.html')
