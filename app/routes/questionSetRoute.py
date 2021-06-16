from fastapi import APIRouter, Depends
from ..schemas.questionSetSchema import QuestionSetSchema, QuestionSetResponseModel
from ..services import (questionSetService)

router = APIRouter()


@router.post("/setQuestions", response_description="Set question", response_model=QuestionSetResponseModel)
def add_question(set_question: QuestionSetSchema):
    return questionSetService.add_question(set_question)


@router.get('/getQuestions', response_description="Get questions")
def get_questions():
    return questionSetService.get_questions()




