import pymongo

mongoURI = "mongodb://localhost:27017"
client = pymongo.MongoClient(mongoURI)
db = client["TODO"]
collection = db["todo"]

def create(data):
    response = collection.insert_one(data)
    return response.inserted_id

def all():
    response = collection.find({})
    return list(response)

def get_one(condition):
    response = collection.find_one({"name": condition})
    return response

def update(name, data):
    response = collection.update_one({"name": name}, {"$set": data})
    return response.modified_count

def delete(name):
    response = collection.delete_one({"name": name})
    return response.deleted_count
