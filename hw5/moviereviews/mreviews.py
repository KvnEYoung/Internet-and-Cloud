# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from moviereviews import get_model
from flask import Blueprint, redirect, render_template, request, url_for


mreviews = Blueprint('mreviews', __name__)

@mreviews.route('/main')
def main():
    return render_template("main.html")

# [START list]
@mreviews.route("/")
def list():
    token = request.args.get('page_token', None)
    moviereviews, next_page_token = get_model().list(cursor=token)

    return render_template(
        "list.html",
        moviereviews=moviereviews,
        next_page_token=next_page_token)
# [END list]


@mreviews.route('/<id>')
def view(id):
    moviereview = get_model().read(id)
    return render_template("view.html", moviereview=moviereview)


# [START add]
@mreviews.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data = request.form.to_dict(flat=True)

        moviereview = get_model().create(data)

        return redirect(url_for('.list', id=moviereview['id']))

    return render_template("form.html", action="Add", moviereview={})
# [END add]


@mreviews.route('/<id>/edit', methods=['GET', 'POST'])
def edit(id):
    moviereview = get_model().read(id)

    if request.method == 'POST':
        data = request.form.to_dict(flat=True)

        moviereview = get_model().update(data, id)

        return redirect(url_for('.list', id=moviereview['id']))

    return render_template("form.html", action="Edit", moviereview=moviereview)


@mreviews.route('/<id>/delete')
def delete(id):
    get_model().delete(id)
    return redirect(url_for('.list'))
