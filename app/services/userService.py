from ..db import loginCollection, studentDetailsCollection
from .authService import AuthHandler
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
from bson.objectid import ObjectId


authService = AuthHandler()
def user_helper(user) -> dict:
    return {
        "type": user["type"],
        "email": user["email"],
        "firstName": user["firstName"]
    }

def studentDetails_helper(user) -> dict:
    return {
        "firstName": user["firstName"],
        "lastName": user["lastName"],
        "division": user["division"],
        "stream": user["stream"],
        "email": user["email"],
        "qPaperDetails": user["qPaperDetails"]
    }

def add_user(user,type):
    find_user = loginCollection.find_one({'email': user.email})
    if(find_user):
        raise HTTPException(status_code=400,
                            detail='Email is already present please sign in')
    elif(user.password != user.confirmPassword):
        raise HTTPException(
            status_code=400,
            detail='Password and Confirm password do not match')
    hashed_password = authService.get_password_hash(user.password)
    user.password = hashed_password
    del user.confirmPassword
    new_user = jsonable_encoder(user)
    new_user["type"] = type
    loginCollection.insert_one(new_user)
    del user.password
    return {"data": user,
            "message": "user created successfully"}

def login_user(authdetails):
    user = None
    currentUser = loginCollection.find_one({'email':authdetails.email})
    if(currentUser):
        user = currentUser
    if(user is None)or(not authService.verify_password(authdetails.password,user["password"])):
        raise HTTPException(
            status_code=401,
            detail = "Invalid Email and/or Password")
    token=authService.encode_token(str(user["_id"]))
    return {"token" : token,"type": user["type"]}

def get_user(userid):
    currentUser = loginCollection.find_one({'_id': ObjectId(userid)})
    return {"data": user_helper(currentUser)}

def get_StudentDetails(userid):
    emailUser = loginCollection.find_one({'_id': ObjectId(userid)})
    currentUser = studentDetailsCollection.find_one({'email': emailUser["email"]})
    #classavg = classDetailsCollection.find_one({'division': emailUser["division"]})
    return {"data": studentDetails_helper(currentUser)}






