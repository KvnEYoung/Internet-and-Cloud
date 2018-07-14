from flask import Flask, redirect, request, url_for, render_template
import MRModels

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/reviews')
def reviews():
    model = MRModels.get_model()
    reviews = model.select()
    return render_template('reviews.html', reviews=reviews)

if __name__ == '__main__':
    app.run(port=8000, debug=True)
