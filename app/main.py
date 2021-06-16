from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes.userRoute import router as UserRouter
from .routes.loginRoute import router as LoginRouter
from .routes.questionPaperRoute import router as QuestionPaperRouter
from .routes.questionSetRoute import router as QuestionSetRouter
from .routes.answerSheetRoute import router as AnswerSheetRouter
from .routes.studentDetailsRoute import router as StudentDetailsRouter
from .routes.classDetailsRoute import router as ClassDetailsRouter
from .routes.notificationsRoute import router as notificationsRouter
app = FastAPI()
origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(UserRouter, tags=["User"], prefix="/user")
app.include_router(LoginRouter, tags=["Login"], prefix="/login")
app.include_router(QuestionPaperRouter, tags=["QuestionPaper"], prefix="/questionPaper")
app.include_router(QuestionSetRouter, tags=["Questions"], prefix="/questions")
app.include_router(AnswerSheetRouter, tags=["AnswerSheet"], prefix="/answerSheet")
app.include_router(StudentDetailsRouter, tags=["StudentDetails"], prefix="/studentDetails")
app.include_router(ClassDetailsRouter, tags=["ClassDetails"], prefix="/classDetails")
app.include_router(notificationsRouter, tags=["notifications"], prefix="/notifications")
@app.get("/")
def readroute():
    return{
        "message": "Hello World"
        }