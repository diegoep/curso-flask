from flask import render_template, current_app
from . import main  # importa o blueprint criado em __init__.py

@main.route('/')
def index():
    posts = current_app.posts
    return render_template('index.html', posts=posts)