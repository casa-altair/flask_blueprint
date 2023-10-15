""" 
Application Configuration File
To define and import variables app wide, import Variables
For logging application, use app_log
"""
from os import environ, path, makedirs
import secrets
import string
import logging
from logging.handlers import TimedRotatingFileHandler
from dotenv import load_dotenv
# ----------------------------------------------------------------------------------------------

# Initialize Files with their locations
app_home_path = path.abspath(path.dirname(__file__))
app_docs_path = app_home_path
load_dotenv(path.join(app_home_path, ".env"))

bool_mapping = {
    "True": True,
    "False": False
}
# ----------------------------------------------------------------------------------------------

def generate_random_string(length):
    """ Create a random string of defined length """
    character_set = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(secrets.choice(character_set) for _ in range(length))
    return random_string
# ----------------------------------------------------------------------------------------------

class Variables:
    """ Define all required variables """
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{app_docs_path}/models/{environ.get('db_file')}"
    print(SQLALCHEMY_DATABASE_URI)
    SECRET_KEY = generate_random_string(int(environ.get("secret_key_length")))
    MQTT_BROKER_URL = environ.get("mqtt_ip")
    MQTT_BROKER_PORT = int(environ.get("mqtt_port"))
    MQTT_BROKER_USERNAME = environ.get("mqtt_username")
    MQTT_BROKER_PASSWORD = environ.get("mqtt_password")
    MQTT_TLS_ENABLED = False
    APP_RUN_PORT = environ.get("app_run_port")
    APP_DEBUG = bool_mapping.get(environ.get("debug"), False)
# ----------------------------------------------------------------------------------------------

# Check if log folder is present
application_log_folder = f"{app_home_path}/application_log"
if not path.exists(application_log_folder):
    makedirs(application_log_folder)

# Configure the logging settings for transaction
app_log = logging.getLogger('app_log')
app_log.setLevel(logging.DEBUG)
log_handler = TimedRotatingFileHandler(
    filename=f'{app_home_path}/log/app.log',
    when='midnight',
    interval=1,
    backupCount=10,
)
log_format = logging.Formatter(
    fmt='%(asctime)s|%(levelname)s|%(message)s',
    datefmt='%d/%m/%Y|%H:%M:%S'
)
log_handler.setFormatter(log_format)
app_log.addHandler(log_handler)
# ----------------------------------------------------------------------------------------------
