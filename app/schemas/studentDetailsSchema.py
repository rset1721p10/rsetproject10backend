from pydantic import BaseModel, EmailStr


class StudentDetailsSchema(BaseModel):
    firstName: str
    lastName: str
    division: str
    stream: str
    email: EmailStr
    qPaperDetails : list

class StudentDetailResponseModel(BaseModel):
    data = {
        "firstName": "str",
        "lastName": "str",
        "division": "str",
        "stream": "str",
        "email": "user@example.com",
        "qPaperDetails": []
    }
    message = "user created successfully"
