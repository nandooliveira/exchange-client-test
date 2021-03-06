# -*- coding: utf-8 -*-
"""Module responsible for managing exchange rate on database."""

from pymongo import MongoClient
import os

MONGO_URL = os.environ.get('MONGO_URL')
if not MONGO_URL:
    MONGO_URL = "159.203.82.71"

class ExchangeRateRepository:
    u"""Repository to persist exchange rates."""

    def __init__(self):
        u"""Initialize repository."""
        self.client = MongoClient(MONGO_URL, 27017)
        self.db = self.client.lotebox
        self.exchange_rates = self.db.exchange_rates

    def save(self, exchange_rate):
        u"""Save method."""
        return self.exchange_rates.insert_one(exchange_rate).inserted_id

    def find(self, limit=None, params={}, sort=[("datetime", -1)]):
        """Find last limit of registries."""
        if limit:
            cursor = self.exchange_rates.find(params).sort(sort)\
                    .limit(int(limit))
        else:
            cursor = self.exchange_rates.find(params).sort(sort)

        exchange_rates = []
        for rate in cursor:
            exchange_rates.append(rate)

        return exchange_rates
