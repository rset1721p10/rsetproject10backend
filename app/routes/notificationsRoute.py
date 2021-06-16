from fastapi import APIRouter, Depends
from ..schemas.notificationsSchema import NotificationsSchema, NotificationsResponseModel
from ..services import (notificationsService)

router = APIRouter()

@router.post("/addNotification", response_description="Add New Notification", response_model=NotificationsResponseModel)
def add_Notifications(register_studentDetails: NotificationsSchema):
    return notificationsService.add_Notification(register_studentDetails)


@router.get('/getSearchedNotification', response_description="Get Searched Notification", response_model=NotificationsResponseModel)
def get_SingleNotification(email):
    return notificationsService.get_SingleNotification(email)

@router.get('/getAllNotifications', response_description="Get All Notifications")
def get_AllNotifications():
    return notificationsService.get_AllNotifications()



