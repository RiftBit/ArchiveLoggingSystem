from app.models.Users import User
from flask import render_template, g, request
from app import app, db


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

@app.before_request
def before_request():
    g.user = User


@app.after_request
def after_request(response):
    return response


@app.route('/')

def index_handler():
    return render_template('index.html', user_hello="Hello!")


@app.route('/logout')
def logout_handler():
    return 'ASD'
