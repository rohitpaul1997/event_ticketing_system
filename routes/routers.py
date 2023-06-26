from fastapi import APIRouter, Request

userRouter = APIRouter( prefix = '/user', tags = ['User_Serverice'] )

@userRouter.post('/register')
async def userRegister(user: Request):
    info = await user.json()
    print(info)


 