#!/usr/bin/env python3
"""lists all documents in a collection"""


def list_all(mongo_collection):
    """
    lists all documents in a mongo collection
    """
    if mongo_collection is None:
        return []

    return list(mongo_collection.find())
