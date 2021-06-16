from fastapi import APIRouter, Depends
from ..schemas.questionPaperSchema import QuestionPaperSchema, QuestionPaperResponseModel
from ..services import (questionPaperService,)

router = APIRouter()


@router.post("/questionPaper", response_description="Set question paper", response_model=QuestionPaperResponseModel)
def add_questionPaper(set_question: QuestionPaperSchema):
    return questionPaperService.add_questionPaper(set_question)


@router.get('/getQuestionPaper', response_description="Get questionpaper")
def get_questionPaper():
    return questionPaperService.get_questionpaper()

@router.get('/getAllQuestionPapers', response_description="Get All Question Papers")
def get_AllQuestionPapers():
    return questionPaperService.get_allQuestionPapers()



