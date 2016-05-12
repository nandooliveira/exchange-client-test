#!env/bin/python
# initialize flask app
u"""Starts development server."""
from app import app, init

init()

app.run(debug=app.config['DEBUG'], host=app.config["HOST"],
        port=app.config["PORT"])
