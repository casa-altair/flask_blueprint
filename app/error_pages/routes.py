from flask import render_template
from . import bp_page_error  # Import the main blueprint

@bp_page_error.app_errorhandler(404)
def error_404(error):
    return render_template('404.html', error=error), 404

@bp_page_error.app_errorhandler(500)
def error_500(error):
    return render_template('500.html', error=error), 500
