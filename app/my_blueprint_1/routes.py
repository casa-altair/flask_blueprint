""" Write all routes for this blueprint """
import secrets
import string
from flask import render_template
from . import blueprint_1  # Import the main blueprint

def generate_random_string(length=10):
    character_set = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(secrets.choice(character_set) for _ in range(length))

    return random_string

@blueprint_1.route('/')
def index():
    from models.models import User  # Import User model within the route function
    from app import db  # Create the db instance within the route function
    # Use User and db as needed
    add_user = User(
        user_name = generate_random_string(),
        user_email = generate_random_string()
    )
    db.session.add(add_user)
    db.session.commit()
    return render_template('bp1_index.html')
