from flask import Blueprint, render_template

admin_bp = Blueprint(
    'admin',
    __name__,
    template_folder='templates',
)

@admin_bp.route('/admin')
def admin_dashboard():
    return render_template('admin/dashboard.html')
