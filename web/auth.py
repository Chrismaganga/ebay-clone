from flask import Blueprint
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return '<p>login</p>'
    
@auth.route('/logout')
def logout():
    return '<p>logout</p>'

@auth.route('/sign-up')
def signup():
    return '<p>sign Up</p>'
    
     

