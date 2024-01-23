#!/usr/bin/env python3
"""inserts a new document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document in a mongo collection based on kwargs
    """
    if mongo_collection is None:
        return None

    newDocument = mongo_collection.insert_one(kwargs)

    return newDocument.inserted_id
