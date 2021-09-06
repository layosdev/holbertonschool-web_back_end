#!/usr/bin/env python3
"""NoSql Module
    """

import pymongo


def list_all(mongo_collection):
    """
    lists all documents in a collection:
    """
    if not mongo_collection:
        return []
    documents = mongo_collection.find()
    return documents
