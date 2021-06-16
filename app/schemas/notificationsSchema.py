from pydantic import BaseModel, EmailStr


class NotificationsSchema(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    notification : str

class NotificationsResponseModel(BaseModel):
    data = {
        "firstName": "str",
        "lastName": "str",
        "email": "user@example.com",
        "notification": "str"
    }
    message = "notification added successfully"
