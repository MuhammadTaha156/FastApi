from fastapi import FastAPI

app=FastAPI()

# @app.post("/create-user")
# def create_user(name: str,age:int):
#     return {
#         "Name":name,
#         "Age":age
#     }

@app.post("/create-user")
def create_user(user: dict):
    return {
        "message":"User Created",
        "data":user
    }

