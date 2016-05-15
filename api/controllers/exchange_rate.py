# -*- coding: utf-8 -*-
u"""ExchangeRate app Controller."""
import json
from flask import Response, Blueprint, request, make_response, jsonify
from ..repository.exchange_rate import ExchangeRateRepository
from ..restclients.exchange_rate import ExchangeRateRestClient
from ..utils.json_encoder import JSONEncoder

exchange_rate = Blueprint('exchange_rate', __name__)


@exchange_rate.route("/api/v1/exchange_rate", methods=["GET"])
def index():
    u"""Main entrypoint."""
    params = {}
    for key in request.args.keys():
        params[key] = {"$regex": unicode(request.args.get(key))}

    repository = ExchangeRateRepository()
    rates = repository.find(params=params)

    return Response(
        JSONEncoder().encode(rates),
        mimetype="application/json"
    )


@exchange_rate.route(
    "/api/v1/exchange_rate/<string:initial_date>/<string:final_date>",
    methods=['GET']
    )
def findByRangeDate(initial_date, final_date):
    u"""Return rates between a specified period."""
    repository = ExchangeRateRepository()

    if initial_date == final_date:
        rates = repository.find(params={"datetime": {
            "$regex": unicode(initial_date)
            }}, sort=[('datetime', 1)])
    elif initial_date > final_date:
        return make_response(jsonify(
            {
                'error':
                'Unprocessable Entity',
                'message':
                'Initial date can not be greater than final date'
            }
        ), 422)
    else:
        rates = repository.find(params={
            "$and": [
                    {"datetime": {"$gte": initial_date}},
                    {"datetime": {"$lte": final_date}}
                ]}, sort=[('datetime', 1)])

    return Response(JSONEncoder().encode(rates),
                    mimetype="application/json")


@exchange_rate.route("/api/v1/exchange_rate/current", methods=["GET"])
def current():
    u"""Main entrypoint."""
    rest_client = ExchangeRateRestClient()
    return Response(
        json.dumps(rest_client.get_exchange_rate()),
        mimetype="application/json"
        )
