from fastapi import APIRouter, Depends
from ..schemas.studentDetailsSchema import StudentDetailsSchema, StudentDetailResponseModel
from ..services import (studentDetailsService,authService,userService)

router = APIRouter()
authService = authService.AuthHandler()

@router.post("/studentDetails", response_description="Student Details Configuration", response_model=StudentDetailResponseModel)
def add_studentDetails(register_studentDetails: StudentDetailsSchema):
    return studentDetailsService.add_studentDetails(register_studentDetails)



@router.get('/getStudentDetails', response_description="Get Logged in Student details", response_model=StudentDetailResponseModel)
def get_StudentDetails(userid=Depends(authService.auth_wrapper)):
    return userService.get_StudentDetails(userid)

@router.get('/getSearchedStudentDetails', response_description="Get Searched Student details", response_model=StudentDetailResponseModel)
def get_SearchedStudentDetails(email):
    return studentDetailsService.get_SingleStudent(email)
@router.get('/getSearchedStudentProgress', response_description="Get Searched Student progress")
def get_SearchedStudentProgress(email):
    return studentDetailsService.get_SingleStudentDetails(email)

@router.get('/getAllStudents', response_description="Get All Students")
def get_AllStudents():
    return studentDetailsService.get_AllStudents()



