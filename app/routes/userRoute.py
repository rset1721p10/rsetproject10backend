from fastapi import APIRouter, Depends
from ..schemas.registerUserSchema import RegisterTeacherSchema, RegisterStudentSchema, RegisterResponseModel, ResetPasswordSchema
from ..services import (userService, authService,)

router = APIRouter()
authService = authService.AuthHandler()


@router.post("/registerTeacher", response_description="Teacher registration", response_model=RegisterResponseModel)
def add_teacher(register_teacher: RegisterTeacherSchema):
    return userService.add_user(register_teacher,"Teacher")

@router.post("/registerStudent", response_description="Student registration", response_model=RegisterResponseModel)
def add_student(register_student: RegisterStudentSchema):
    return userService.add_user(register_student,"Student")





# @router.put('/forgotPassword', response_description="Reset users password", response_model=ResetPasswordResponseModel)
# def reset_password(reset_password: ResetPasswordSchema):
#     return user_service.reset_password(reset_password)


