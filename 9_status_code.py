from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel

app=FastAPI()

@app.post("/create_user",status_code=status.HTTP_201_CREATED)
def creare_user():
    return {
        "message":"User Created"
    }

@app.get("/user")
def get_user():
    return{
        "status":"Success",
        "message":"User Fetched",
        "Data":{
            "name":"Taha",
            "Age":21
        }
    }

@app.get("/users/{user_id}")
def get_user(user_id:int):
    if user_id !=1:
        raise HTTPException(
            status_code=404,
            detail="User not Found"
        )
    return {
        "Id":1,
        "name":"Taha"
    }

