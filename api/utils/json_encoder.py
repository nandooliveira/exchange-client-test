# -*- coding: utf-8 -*-
"""Json Serializer."""
import json
from bson import ObjectId


class JSONEncoder(json.JSONEncoder):
    """Class responsible to serialize a json returned from mongodb."""

    def default(self, o):
        """Default Serializer."""
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
