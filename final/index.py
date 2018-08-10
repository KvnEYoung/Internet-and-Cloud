from flask import render_template, request
from flask.views import MethodView
import movie_models as mm

class index(MethodView):
    def get(self):
        """
        Renders landing page for movie review site.
        """
        model = mm.get_model()
        language = model.getLanguage()
        return render_template('index.html', language=language)
        
    def post(self):
        """
        POST request to process form data to change the language of reviews.
        """
        model = mm.get_model()
        language = request.form['review_lang']
        model.setLanguage(language)
        return render_template('index.html', language=model.getLanguage())
