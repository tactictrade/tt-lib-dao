from pymongo import MongoClient

def database(dbName='', config={}):

    # Connect to MongoDB
    client = MongoClient(config['TT_MONGO_DB_URI'])
    dbname = client.get_database()
    collection_name = dbname[dbName]

    return client, dbname, collection_name