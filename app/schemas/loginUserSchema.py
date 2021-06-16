from pydantic import BaseModel, EmailStr


class LoginUserSchema(BaseModel):
    email: EmailStr
    password: str

class ResetPasswordSchema(BaseModel):
    email: EmailStr
    password: str
    confirmPassword: str


class LoginResponseModel(BaseModel):
    data = {
        "firstName": "str",
        "lastName": "str",
        "email": "user@example.com"
    }
    message = "Logged ON successfully"
