""" WSGI.py: Run this application to start server """

from gevent.pywsgi import WSGIServer
from app import create_app
from config import Variables

app = create_app()

if __name__ == "__main__":
    if Variables.APP_DEBUG:
        app.run(host="0.0.0.0", port=Variables.APP_RUN_PORT, debug=Variables.APP_DEBUG)
    else:
        app_server = WSGIServer(('0.0.0.0', Variables.APP_RUN_PORT), app)
        app_server.serve_forever()
