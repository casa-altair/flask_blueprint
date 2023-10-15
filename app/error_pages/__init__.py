from flask import Blueprint

# Create the main blueprint
bp_page_error = Blueprint(
    'bp_page_error',
    __name__,
    template_folder='templates'
)

# Import views or routes specific to the main part of your application
from . import routes
