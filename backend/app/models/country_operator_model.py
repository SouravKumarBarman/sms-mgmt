from pymongo import MongoClient
from app.config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client["sms_db"]

def add_country_operator(country, operator, high_priority):
    data = {"country": country, "operator": operator, "high_priority": high_priority, "status": "active"}
    db.country_operators.insert_one(data)
    return {"message": "Country-operator pair added"}

def update_country_operator(country, operator, status):
    db.country_operators.update_one({"country": country, "operator": operator}, {"$set": {"status": status}})
    return {"message": "Status updated"}

def delete_country_operator(country, operator):
    db.country_operators.delete_one({"country": country, "operator": operator})
    return {"message": "Country-operator pair deleted"}
