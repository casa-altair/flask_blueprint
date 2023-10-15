from flask import render_template
from . import blueprint_2  # Import the main blueprint

@blueprint_2.route('/')
def home():
    from models.models import User  # Import User model within the route function
    from app import db  # Create the db instance within the route function
    # Use User and db as needed
    return render_template('bp2_index.html')
