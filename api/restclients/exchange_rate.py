# -*- coding: utf-8 -*-
u"""Module responsible to load exchange rates from rest api."""
import requests
from base import BaseRestClient
from api.repository.exchange_rate import ExchangeRateRepository
from datetime import datetime


class ExchangeRateRestClient(BaseRestClient):
    u"""Class to make request to exchange rates."""

    def get_exchange_rate(self):
        u"""Fetch json from server."""
        r = requests.get('%scurrencies/real/exchange-rate/' % self.BASE_URL)
        return r.json()

    def load_exchange_rate(self):
        u"""Job to get json fron server every 5 seconds.

        Get data from REST Api and save it on database
        """
        repository = ExchangeRateRepository()

        exchange_rates = self.get_exchange_rate()
        repository.save({"datetime": datetime.now().isoformat(),
                         "rates": exchange_rates})
