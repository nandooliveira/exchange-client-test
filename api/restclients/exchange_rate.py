# -*- coding: utf-8 -*-
u"""Module responsible to load exchange rates from rest api."""
import requests
from base import BaseRestClient


class ExchangeRateRestClient(BaseRestClient):
    u"""Class to make request to exchange rates."""

    def get_exchange_rate(self):
        u"""Fetch json from server."""
        r = requests.get('%scurrencies/real/exchange-rate/' % self.BASE_URL)
        return r.json()
