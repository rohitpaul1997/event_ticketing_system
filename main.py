from fastapi import FastAPI 

#importing routes
from routes import routers

userReg = FastAPI()

@userReg.get('/')
def mainRoute():
    return {"Hello"}

#including routes
userReg.include_router(routers.userRouter)    