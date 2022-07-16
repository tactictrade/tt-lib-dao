# from dao.UserDao import UserDao
from pymongo import MongoClient
import os
# from dao.utils.mongoDatabase import database

def database(dbName='', config={}):

    # Connect to MongoDB
    client = MongoClient(config['TT_MONGO_DB_URI'])
    dbname = client.get_database()
    collection_name = dbname[dbName]

    return client, dbname, collection_name

class UserDao():
# class UserDao(UserDao): #TODO check this

    def __init__(self, config={}):
        super().__init__()
        # Connect to MongoDB
        self.client, self.dbname, self.collection_name = database("user", config)

    def create(self,userDto):
        # Create user in MongoDB
        result = self.collection_name.insert_one(userDto)
        print(f'User {result} created in Mongo!!!!')
        return result

    def find(self, query={}):
        
        # Read user from MongoDB
        result = self.collection_name.find(query)

        print(f'User {result} readed in Mongo!!!!')
        return result

    def find_one(self, query={}):
        
        # Read user from MongoDB
        result = self.collection_name.find_one(query)

        print(f'User {result} readed in Mongo!!!!')
        return result
    
    def update_one(self,filterQuery={}, updateData={}):

        result = self.collection_name.update_one(filterQuery,updateData)
        print(f'User {result} update in Mongo!!!!')

        return result

    def update(self,filterQuery={}, updateData={}):

        result = self.collection_name.update(filterQuery,updateData)

        print(f'User {result} update in Mongo!!!!')

        return result

    def delete(self,query={}):

        result = self.collection_name.update(query)

        print(f'User {result} update in Mongo!!!!')

        return result



