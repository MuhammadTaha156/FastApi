from fastapi import FastAPI,status,HTTPException,Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app=FastAPI()

# @app.get("/users/{user_id}")
# def get_user(user_id:int):
#     if user_id !=1:
#         raise HTTPException(status_code=404,
#                             detail="User not Found")
    
#     return {"id":1,
#             "name":"Mohit"}

#                                            #Custom Exception/Error
# class User_Not_Found_Exception(Exception):
#     def __init__(self, name:str):
#         self.name=name

# @app.get("/users/{name}")
# def get_user(name:str):
#     if name != "taha":
#         raise User_Not_Found_Exception(name)
#     return{
#         "Name":name
#     }





#Custom Exception/Error
class User_Not_Found_Exception(Exception):
    def __init__(self, name:str):
        self.name=name

@app.exception_handler(User_Not_Found_Exception)
def user_not_found_handler(request:Request,exc:User_Not_Found_Exception):
    return JSONResponse(
        status_code=404,
        content={
            "status":"error",
            "message":f"User {exc.name} not found"
        }
    )

@app.get("/users/{name}")
def get_user(name:str):
    if name != "taha":
        raise User_Not_Found_Exception(name)
    return{
        "Name":name
    }

