from pydantic import BaseModel


class ClassDetailSchema(BaseModel):
    division: str
    stream: str
    qPaperDetails: list


class ClassDetailResponseModel(BaseModel):
    data = {
        "division": "str",
        "stream": "str",
        "qPaperDetails" : "list"
    }
    message = "Class created successfully"
