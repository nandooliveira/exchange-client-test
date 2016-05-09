# -*- coding: utf-8 -*-
u"""ExchangeRate app Controller."""
from flask import Response, Blueprint
from repository.exchange_rate import ExchangeRateRepository
from utils.json_encoder import JSONEncoder

exchange_rate = Blueprint('exchange_rate', __name__)


@exchange_rate.route("/api/v1/exchange_rate", methods=["GET"])
def index():
    u"""Main entrypoint."""
    repository = ExchangeRateRepository()
    rates = repository.find()

    return Response(
        JSONEncoder().encode(rates),
        mimetype="application/json"
    )
