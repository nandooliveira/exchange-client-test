#!env/bin/python
# -*- coding: utf-8 -*-
u"""Main Module."""
from datetime import datetime
import time
import os
import logging

from flask import Flask, make_response, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
from restclients.exchange_rate import ExchangeRateRestClient
from repository.exchange_rate import ExchangeRateRepository

from controllers.exchange_rate import exchange_rate
from flask.ext.cors import CORS

logging.basicConfig()

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.debug = False
CORS(app)


def load_exchange_rate():
    u"""Job to get json fron server every 5 seconds.

    Get data from REST Api and save it on database
    """
    print time.strftime('%H:%M:%S')
    rest_client = ExchangeRateRestClient()
    repository = ExchangeRateRepository()

    exchange_rates = rest_client.get_exchange_rate()
    repository.save({"datetime": datetime.now().isoformat(),
                     "rates": exchange_rates})


def init():
    u"""Initializer."""
    # initialize Cron scheduler
    if not app.debug or os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        cron = BackgroundScheduler(daemon=True)
        cron.start()
        cron.add_job(load_exchange_rate, 'interval',
                     minutes=app.config["FETCH_DURATION_IN_MINUTES"],
                     id='exg_rate')

    # register our blueprints
    app.register_blueprint(exchange_rate)

    # app.run(debug=app.config['DEBUG'], host=app.config["HOST"],
    #         port=app.config["PORT"])


@app.errorhandler(404)
def not_found(error):
    u"""Not found handler."""
    return make_response(jsonify({'error': 'Not found'}), 404)

init()
