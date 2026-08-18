from pymongo import MongoClient
from pymongo.errors import PyMongoError


class AnimalShelter:
    """CRUD operations for the AAC animal database."""

    def __init__(self, username, password):
        """Connect to MongoDB."""
        self.client = MongoClient(
            host="localhost",
            port=27017,
            username=username,
            password=password,
            authSource="aac"
        )

        self.database = self.client["aac"]
        self.collection = self.database["animals"]

    def create(self, data):
        """Insert one document into the collection."""
        if not data:
            return False

        try:
            self.collection.insert_one(data)
            return True
        except PyMongoError as error:
            print("Create error:", error)
            return False

    def read(self, query):
        """Find and return documents as a list."""
        try:
            results = self.collection.find(query)
            return list(results)
        except PyMongoError as error:
            print("Read error:", error)
            return []

    def update(self, query, update_data):
        """Update all documents matching the query."""
        try:
            result = self.collection.update_many(query, update_data)
            return result.modified_count
        except PyMongoError as error:
            print("Update error:", error)
            return 0

    def delete(self, query):
        """Delete all documents matching the query."""
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except PyMongoError as error:
            print("Delete error:", error)
            return 0
