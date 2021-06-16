from pymongo.message import update
from ..db import questionPapersCollection,studentDetailsCollection,classDetailsCollection,answersheetCollection,notificationsCollection
from fastapi.encoders import jsonable_encoder

def questionpaper_helper(question) -> dict:
    return {
        "qpId": question["qpId"],
        "serial": question["serial"],
        "date": question["date"],
        "time": question["time"],
        "duration": question["duration"],
        "questions": question["questions"],
        "marks" : question["marks"],
        "latest" : question["latest"]
    }
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
def add_questionPaper(questionPaper):
    dbstudentlist = studentDetailsCollection.find()
    dbclasslist = classDetailsCollection.find()
    questionPaperSet = questionPapersCollection.find()
    questionPaperlist=[]
    for i in questionPaperSet:
        questionPaperlist.append(questionpaper_helper(i))
    studentlist=[]
    for i in dbstudentlist:
        studentlist.append(studentDetails_helper(i))
    classlist=[]
    for i in dbclasslist:
        classlist.append(classDetails_helper(i))
    if(len(questionPaperlist)>0):
        updateLatestQuestionPaper(questionPaperlist)
    next_questionPaper = jsonable_encoder(questionPaper)
    questionPapersCollection.insert_one(next_questionPaper)
    updateStudents(studentlist,next_questionPaper["qpId"])
    updateClass(classlist,next_questionPaper["qpId"])
    dbAnswerSheetRefresh=answersheetCollection.delete_many({})
    notificationsCollection.delete_many({})
    return {"data": questionPaper,
            "message": "question paper created successfully"+'\n'+dbAnswerSheetRefresh.deleted_count+" Answersheets Cleared"}


def updateLatestQuestionPaper(questionPaperlist):
    finalQuestionpaper=len(questionPaperlist)-1
    newValues={"$set":{"latest":False}}
    filter = {"qpId":questionPaperlist[finalQuestionpaper]["qpId"]}
    questionPapersCollection.update_one(filter,newValues)

def updateStudents(studentlist,qpid):
    for i in studentlist:
        i["qPaperDetails"].append({
        "qPaperId": qpid,
        "levelOfUnderstanding1": 0,
        "levelOfUnderstanding2": 0,
        "sdmarks1": 0,
        "sdmarks2": 0,
        "sdtotalMarks": 0
    })
        newValues={"$set":i}
        filter = {"email":i["email"]}
        studentDetailsCollection.update_one(filter,newValues)

def updateClass(classlist,qpid):
    for i in classlist:
        i["qPaperDetails"].append({
        "qPaperId": qpid,
        "cdmarks1": 0,
        "cdmarks2": 0,
        "studentsAttended": 0
    })  
        newValues={"$set":i}
        filter = {"division":i["division"]}
        classDetailsCollection.update_one(filter,newValues)

def get_questionpaper():
    questionPaperSet = questionPapersCollection.find()
    questionPaperlist=[]
    for i in questionPaperSet:
        questionPaperlist.append(questionpaper_helper(i))
    result=[]
    if(len(questionPaperlist)!=0):
        finalQuestionpaper=len(questionPaperlist)-1
        result.append(questionpaper_helper(questionPaperlist[finalQuestionpaper]))
    return {"data": result}

def get_allQuestionPapers():
    questionpaperSet = questionPapersCollection.find()
    result=[]
    for i in questionpaperSet:
        result.append(questionpaper_helper(i))
    return {"data": result}


