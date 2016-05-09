# -*- coding: utf-8 -*-
"""Module responsible for managing exchange rate on database."""

from pymongo import MongoClient


class ExchangeRateRepository:
    u"""Repository to persist exchange rates."""

    def __init__(self):
        u"""Initialize repository."""
        self.client = MongoClient('192.168.0.14', 27017)
        self.db = self.client.lotebox
        self.exchange_rates = self.db.exchange_rates

    def save(self, exchange_rate):
        u"""Save method."""
        return self.exchange_rates.insert_one(exchange_rate).inserted_id

    def find(self, limit=None):
        """Find last limit of registries."""
        if limit:
            cursor = self.exchange_rates.find().sort({"_id": 1}).limit(limit)
        else:
            cursor = self.exchange_rates.find()

        exchange_rates = []
        for rate in cursor:
            exchange_rates.append(rate)

        return exchange_rates
