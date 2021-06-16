from pydantic import BaseModel, EmailStr


class AnswerSheetSchema(BaseModel):
    userid: EmailStr
    qpId: str
    question : list
    types : dict
    entries: dict
    marks: dict
    levelOfUnderstanding1: int
    levelOfUnderstanding2: int
    marks1: int
    marks2: int
    totalMarks: int



class AnswerSheetResponseModel(BaseModel):
    data = {
        "userid" : "user@example.com",
        "question" : "list",
        "types":"dict",
        "entries": "dict",
        "marks":"dict",
        "levelOfUnderstanding1": "int",
        "levelOfUnderstanding2": "int",
        "marks1": "int",
        "marks2": "int",
        "totalMarks": "int"
    }
    message = "Answer Sheet added successfully"
