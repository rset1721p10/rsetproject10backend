from pydantic import BaseModel
from datetime import date, time


class QuestionPaperSchema(BaseModel):
    qpId: str
    serial: int
    date: date
    time: time
    duration : int
    questions: list
    marks : int
    latest : bool


class QuestionPaperResponseModel(BaseModel):
    data = {
        "qpid": "str",
        "serial" : "int",
        "date": "date",
        "time": "time",
        "duration" : "int",
        "questions": "list",
        "marks" : "int"
    }
    message = "Question Paper created successfully"
