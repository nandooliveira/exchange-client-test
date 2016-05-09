# -*- coding: utf-8 -*-
u"""Main app Controller."""
from flask import Response, Blueprint
from restclients.exchange_rate import ExchangeRateRestClient

main = Blueprint('main', __name__)


@main.route("/api/v1", methods=["GET"])
def main():
    u"""Main entrypoint."""
    rest_client = ExchangeRateRestClient()

    return Response(
        rest_client.get_exchange_rate(),
        mimetype="application/json"
        )
