from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from . import db
from .models import Upcoming_matches
from .matches import complete_matches

main = Blueprint('main', __name__)
    
@main.route('/')
def index():

    if not Upcoming_matches.query.first() : # check if table is empty
        complete_matches()
        
    return render_template('index.html', Upcoming_matches=Upcoming_matches.query.all() )

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/topbet')
def topbet():
    return render_template('topbet.html')