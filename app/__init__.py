""" Initiaze the application with sql, flask_mqtt, blueprints"""
from flask import Flask
from flask_mqtt import Mqtt
from flask_sqlalchemy import SQLAlchemy
from config import Variables

db = SQLAlchemy()
mqtt = Mqtt()

def create_app():
    """ Create and bind application """
    app = Flask(__name__)

    # Configure SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = Variables.SQLALCHEMY_DATABASE_URI
    db.init_app(app)

    # Configure MQTT
    app.config['SECRET_KEY'] = app.config["SECRET_KEY"]
    app.config['MQTT_BROKER_URL'] = Variables.MQTT_BROKER_URL
    app.config['MQTT_BROKER_PORT'] = int(Variables.MQTT_BROKER_PORT)
    app.config['MQTT_USERNAME'] = Variables.MQTT_BROKER_USERNAME
    app.config['MQTT_PASSWORD'] = Variables.MQTT_BROKER_PASSWORD
    app.config['MQTT_KEEPALIVE'] = 60
    app.config['MQTT_TLS_ENABLED'] = False
    app.config['MQTT_DEBUG'] = True
    mqtt.init_app(app)

    # Import and register blueprints
    # Register the blueprints
    from app.my_blueprint_1 import blueprint_1
    app.register_blueprint(blueprint_1, url_prefix='/blueprint_1')

    from app.my_blueprint_2 import blueprint_2
    app.register_blueprint(blueprint_2, url_prefix='/blueprint_2')

    from app.error_pages import bp_page_error
    app.register_blueprint(bp_page_error)

    # Import models and create database tables
    from models import models
    with app.app_context():
        db.create_all()

    return app
