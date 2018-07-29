""" This is a Movie Review flask application. """
from moviereviews import get_model
from flask import Blueprint, redirect, render_template, request, url_for

mreviews = Blueprint('mreviews', __name__)

""" Function decorator using app.route ( '/', main() ). """
@mreviews.route("/")
def main():
    """ Main movie review webpage. """
    return render_template("main.html")

@mreviews.route('/list')
def list():
    """ Displays all the movie reviews within a webpage. """
    token = request.args.get('page_token', None)
    moviereviews, next_page_token = get_model().list(cursor=token)

    return render_template("list.html", moviereviews=moviereviews,
        next_page_token=next_page_token)

@mreviews.route('/<id>')
def view(id):
    """ Webpage to view individual movie reviews. """
    moviereview = get_model().read(id)
    return render_template("view.html", moviereview=moviereview)

@mreviews.route('/add', methods=['GET', 'POST'])
def add():
    """ Webpage form is called to add a new movie review. POST requests will process the form
     and return to the list page. """
    if request.method == 'POST':
        data = request.form.to_dict(flat=True)
        moviereview = get_model().create(data)
        return redirect(url_for('.list', id=moviereview['id']))

    return render_template("form.html", action="Add", moviereview={})

@mreviews.route('/<id>/edit', methods=['GET', 'POST'])
def edit(id):
    """ Webpage form is called to edit a movie review. POST requests will process the form
     to edit the movie review and return to the list page. """
    moviereview = get_model().read(id)

    if request.method == 'POST':
        data = request.form.to_dict(flat=True)
        moviereview = get_model().update(data, id)
        return redirect(url_for('.list', id=moviereview['id']))

    return render_template("form.html", action="Edit", moviereview=moviereview)

@mreviews.route('/<id>/delete')
def delete(id):
    """ View webpage function to delete a movie review. Movie review id is used to delete 
    the review from the Datastore and return to the list page. """
    get_model().delete(id)
    return redirect(url_for('.list'))
