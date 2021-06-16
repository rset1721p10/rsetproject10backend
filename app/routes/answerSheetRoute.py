from fastapi import APIRouter, Depends
from ..schemas.answerSheetSchema import AnswerSheetSchema, AnswerSheetResponseModel
from ..services import (answerSheetService,)

router = APIRouter()


@router.post("/answerSheet", response_description="Add AnswerSheet", response_model=AnswerSheetResponseModel)
def add_questionPaper(set_answerSheet: AnswerSheetSchema):
    return answerSheetService.add_answerSheet(set_answerSheet)

@router.post("/updateAnswerSheet", response_description="Update AnswerSheet", response_model=AnswerSheetResponseModel)
def update_Answersheet(set_answerSheet: AnswerSheetSchema):
    return answerSheetService.update_Answersheet(set_answerSheet)

@router.get('/getanswerSheet', response_description="Get Answer Sheets")
def get_answerSheet():
    return answerSheetService.get_answerSheets()

@router.get('/getSearchedAnswerSheet', response_description="Get Searched Student details", response_model=AnswerSheetResponseModel)
def get_SearchedAnswerSheet(email):
    return answerSheetService.get_SingleAnswerSheet(email)



