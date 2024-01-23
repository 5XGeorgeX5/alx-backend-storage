#!/usr/bin/env python3
"""provides some stats about Nginx logs stored in MongoDB"""


from pymongo import MongoClient


def log_stats():
    """
    provides some stats about Nginx logs stored in MongoDB
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    print(f"{logs.count_documents({})} logs")
    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in http_methods:
        count = logs.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    status = logs.count_documents({"method": "GET", "path": "/status"})
    print(f"{status} status check")


if __name__ == "__main__":
    log_stats()
