#!/usr/bin/env python3
"""NoSql Module
    """

from pymongo import MongoClient


def logger(method):
    """Logs

    Args:
        method (str): method

    Returns:
        int: logs
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_logs = client.logs.nginx
    return nginx_logs.count_documents(method)


if __name__ == "__main__":
    """
    provides some stats about Nginx logs stored in MongoDB:
    """
    print("{} logs".format(logger({})))
    print("Methods:")
    print("\tmethod GET: {}".format(logger({'method': 'GET'})))
    print("\tmethod POST: {}".format(logger({'method': 'POST'})))
    print("\tmethod PUT: {}".format(logger({'method': 'PUT'})))
    print("\tmethod PATCH: {}".format(logger({'method': 'PATCH'})))
    print("\tmethod DELETE: {}".format(logger({'method': 'DELETE'})))
    print("{} status check".format(logger(
        {'method': 'GET', 'path': '/status'}
        )))
