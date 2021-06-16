from fastapi import APIRouter, Depends
from ..schemas.classDetailsSchema import ClassDetailSchema, ClassDetailResponseModel
from ..services import (classDetailsService)

router = APIRouter()

@router.post("/setClassDetails", response_description="Class Details Configuration", response_model=ClassDetailResponseModel)
def add_classDetails(register_classDetails: ClassDetailSchema):
    return classDetailsService.add_classDetails(register_classDetails)

@router.get('/getSearchedClassDetails', response_description="Get Searched Student details", response_model=ClassDetailResponseModel)
def get_SearchedClassDetails(division):
    return classDetailsService.get_OneClass(division)

@router.get('/getAllClasses', response_description="Get All Classes")
def get_AllClasses():
    return classDetailsService.get_AllClasses()





