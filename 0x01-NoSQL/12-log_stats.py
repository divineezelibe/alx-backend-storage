#!/usr/bin/env python3
"""
Aggregation operations
"""
from pymongo import MongoClient

# Connect to the MongoDB database
client = MongoClient()
db = client.logs
collection = db.nginx

# Count the total number of documents
total_logs = collection.count_documents({})

# Count the number of documents for each HTTP method
http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {method: collection.count_documents({"method": method}) for method in http_methods}

# Count the number of documents with method=GET and path=/status
status_path_count = collection.count_documents({"method": "GET", "path": "/status"})

# Display the statistics in the exact format
print(f"{total_logs} logs")
print("Methods:")
for method in http_methods:
    print(f"\tmethod {method}: {method_counts[method]}")
print(f"{status_path_count} status check")

# Close the MongoDB connection
client.close()
