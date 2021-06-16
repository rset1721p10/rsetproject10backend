from pydantic import BaseModel


class QuestionSetSchema(BaseModel):
    qId: str
    question: str
    type: str
    answer: list
    markDistribution: list
    QtotalMarks : int


class QuestionSetResponseModel(BaseModel):
    data = {
        "qId": "str",
        "question": "str",
        "answer": "list",
        "markDistribution" : "list",
        "QtotalMarks" : "int"
    }
    message = "user created successfully"
