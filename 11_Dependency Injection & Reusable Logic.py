from fastapi import FastAPI,status,HTTPException,Request,Depends,Header
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app=FastAPI()

# def common_logic():
#     return {
#         "message":"Common Logic Executed"
#     }

# @app.get("/")
# def hone(data=Depends(common_logic)):
#     return data

#                                                         # Reuseable Logic

# def get_current_users():
#     return {
#         "User":"Taha"
#     }

# @app.get("/profile")
# def profile(user=Depends(get_current_users)):
#     return user

# @app.get("/dashboard")
# def dashboard(user=Depends(get_current_users)):
#     return user

## Real Life Example
def varify_token(token:str=Header(None)):
    if token !="MysercetToken":
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )
    return {
        "User":"Authorized User"
    }

@app.get("/secure_data")
def secure_data(user=Depends(varify_token)):
    return {
        "message":"Secure Data Accessed",
        "User":user
    }