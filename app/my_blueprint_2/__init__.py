from flask import Blueprint

# Create the main blueprint
blueprint_2 = Blueprint(
    'blueprint_2',
    __name__,
    template_folder='templates'
)

# Import views or routes specific to the main part of your application
from . import routes
