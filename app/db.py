import pymongo
import os
from pymongo import MongoClient
from dotenv import dotenv_values,find_dotenv
config = dotenv_values(find_dotenv())
MongoURL = os.environ.get("mongoUrl") or config["mongoUrl"]
loginCollectionConfig = os.environ.get("login") or config["login"]
questionPapersCollectionConfig = os.environ.get("questionpapers") or config["questionpapers"]
questionsCollectionConfig = os.environ.get("questions") or config["questions"]
answerSheetCollectionConfig = os.environ.get("answersheets") or config["answersheets"]
studentDetailsCollectionConfig = os.environ.get("studentDetails") or config["studentDetails"]
classDetailsCollectionConfig = os.environ.get("classDetails") or config["classDetails"]
notificationsCollectionConfig = os.environ.get("notifications") or config["notifications"]
dbCollectionConfig = os.environ.get("database") or config["database"]
cluster = MongoClient(MongoURL)
db = cluster[dbCollectionConfig]
loginCollection =  db[loginCollectionConfig]
questionPapersCollection =  db[questionPapersCollectionConfig]
questionsCollection =  db[questionsCollectionConfig]
answersheetCollection =  db[answerSheetCollectionConfig]
studentDetailsCollection =  db[studentDetailsCollectionConfig]
classDetailsCollection =  db[classDetailsCollectionConfig]
notificationsCollection =  db[notificationsCollectionConfig]