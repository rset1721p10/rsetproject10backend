from fastapi import APIRouter, Depends
from ..schemas.loginUserSchema import LoginUserSchema,  LoginResponseModel, ResetPasswordSchema
from ..services import (userService, authService)

router = APIRouter()
authService = authService.AuthHandler()



@router.post("/login", response_description="User login")
def login_user(login_user: LoginUserSchema):
    return userService.login_user(login_user)



@router.get('/getUser', response_description="Get Logged in User details")
def get_user(userid=Depends(authService.auth_wrapper)):
    return userService.get_user(userid)



# @router.put('/forgotPassword', response_description="Reset users password", response_model=ResetPasswordResponseModel)
# def reset_password(reset_password: ResetPasswordSchema):
#     return user_service.reset_password(reset_password)


