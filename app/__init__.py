
from flask import Flask
from .main.routes import main_bp
from .admin.routes import admin_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp)

    return app
"""

import os
from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register blueprints dynamically
    for foldername in os.listdir(os.path.dirname(__file__)):
        if os.path.isdir(os.path.join(os.path.dirname(__file__), foldername)) and foldername != "__pycache__" and foldername != "templates" and foldername != "static":
            module_name = f"app.{foldername}.routes"
            blueprint = __import__(module_name, fromlist=['app'])

            if hasattr(blueprint, "bp"):
                app.register_blueprint(blueprint.bp)

    return app
"""