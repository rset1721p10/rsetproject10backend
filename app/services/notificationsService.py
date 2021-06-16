from ..db import notificationsCollection
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId
def notifications_helper(studentDetails) -> dict:
    return {
        "firstName": studentDetails["firstName"],
        "lastName": studentDetails["lastName"],
        "email": studentDetails["email"],
        "notification": studentDetails["notification"]
    }
def add_Notification(notification):
    next_notification = jsonable_encoder(notification)
    notificationsCollection.insert_one(next_notification)
    return {"data": notification,
            "message": "student details configured successfully"}

def get_SingleNotification(email):
    result=notificationsCollection.find_one({'email': email})
    return {"data": notifications_helper(result)}

def get_AllNotifications():
    notifications = notificationsCollection.find()
    result=[]
    for i in notifications:
        result.append(notifications_helper(i))
    return {"data": result}



