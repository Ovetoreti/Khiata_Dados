from dotenv import load_dotenv
import os
from pymongo import MongoClient

# Load environment variables from .env file
load_dotenv()

mongo_uri = os.getenv('URI_MONGO')

print("MongoDB URI:", mongo_uri)  # Print URI for verification

try:
    # Connect to MongoDB
    client = MongoClient(mongo_uri)
    print("Connected to MongoDB.")

    # Access specific database
    db = client['Khiata']
    print("Database 'Khiata' accessed successfully.")
    
    print('collections: ', db.list_collection_names())

except Exception as e:
    print("Failed to connect to MongoDB:", e)