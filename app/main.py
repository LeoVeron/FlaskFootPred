from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)
    
@main.route('/')
def index():
    return render_template('index.html')


@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/topbet')
def topbet():
    return render_template('topbet.html')