from flask import Blueprint
from flask_login import login_required, current_user


views = Blueprint('views', __name__)


@views.route('/')
def home():
    return '<h2>HomePage</h2>'
    
       
