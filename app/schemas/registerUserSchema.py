from pydantic import BaseModel, EmailStr


class RegisterTeacherSchema(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    password: str
    confirmPassword: str

class RegisterStudentSchema(BaseModel):
    firstName: str
    lastName: str
    division: str
    stream: str
    email: EmailStr
    password: str
    confirmPassword: str

class ResetPasswordSchema(BaseModel):
    email: EmailStr
    password: str
    confirmPassword: str


class RegisterResponseModel(BaseModel):
    data = {
        "firstName": "str",
        "lastName": "str",
        "email": "user@example.com"
    }
    message = "user created successfully"
