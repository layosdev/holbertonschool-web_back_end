#!/usr/bin/env python3
"""NoSql Module
    """

import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document in a collection based on kwargs
    """
    insert_id = mongo_collection.insert(kwargs)
    return insert_id
