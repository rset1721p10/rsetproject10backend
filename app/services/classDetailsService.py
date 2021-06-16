from ..db import classDetailsCollection
from fastapi.encoders import jsonable_encoder

def classDetails_helper(classDetails) -> dict:
    return {
        "division": classDetails["division"],
        "stream": classDetails["stream"],
        "qPaperDetails": classDetails["qPaperDetails"],
    }
def add_classDetails(classDetails):
    next_class = jsonable_encoder(classDetails)
    classDetailsCollection.insert_one(next_class)
    return {"data": classDetails,
            "message": "class details configured successfully"}

def get_AllClasses():
    AllStudents = classDetailsCollection.find()
    result=[]
    for i in AllStudents:
        result.append(classDetails_helper(i))
    return {"data": result}

def get_OneClass(division):
    result = classDetailsCollection.find_one({'division': division})
    return {"data": classDetails_helper(result)}


