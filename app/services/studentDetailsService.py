from pymongo import results
from ..db import studentDetailsCollection,classDetailsCollection
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId
def studentDetails_helper(studentDetails) -> dict:
    return {
        "firstName": studentDetails["firstName"],
        "lastName": studentDetails["lastName"],
        "division": studentDetails["division"],
        "stream": studentDetails["stream"],
        "email": studentDetails["email"],
        "qPaperDetails": studentDetails["qPaperDetails"],
    }
def classDetails_helper(classDetails) -> dict:
    return {
        "division": classDetails["division"],
        "stream": classDetails["stream"],
        "qPaperDetails": classDetails["qPaperDetails"],
    }
def add_studentDetails(studentDetails):
    next_student = jsonable_encoder(studentDetails)
    studentDetailsCollection.insert_one(next_student)
    return {"data": studentDetails,
            "message": "student details configured successfully"}

def get_SingleStudent(email):
    result=studentDetailsCollection.find_one({'email': email})
    return {"data": studentDetails_helper(result)}

def get_SingleStudentDetails(email):
    result=[]
    sresult=studentDetailsCollection.find_one({'email': email})
    studDetails=studentDetails_helper(sresult)
    cresult=classDetailsCollection.find_one({'division': studDetails['division']})
    classDetails=classDetails_helper(cresult)

    result.append(studDetails)
    result.append(classDetails)
    return {"data": result}

def get_AllStudents():
    AllStudents = studentDetailsCollection.find()
    result=[]
    for i in AllStudents:
        result.append(studentDetails_helper(i))
    return {"data": result}



