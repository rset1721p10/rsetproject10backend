from ..db import questionsCollection
from fastapi.encoders import jsonable_encoder

def question_helper(question) -> dict:
    return {
        "qId": question["qId"],
        "question": question["question"],
        "type": question["type"],
        "answer": question["answer"],
        "markDistribution": question["markDistribution"],
        "QtotalMarks" : question["QtotalMarks"]
    }

def add_question(question):
    next_question = jsonable_encoder(question)
    questionsCollection.insert_one(next_question)
    return {"data": question,
            "message": "question paper created successfully"}



def get_questions():
    questionSet = questionsCollection.find()
    result=[]
    for i in questionSet:
        result.append(question_helper(i))
    return {"data": result}





