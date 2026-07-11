from fastapi import FastAPI

app=FastAPI()

#User Route
@app.get("/users/{user_id}")
def get_users(user_id:int):
    return {"user_id":user_id}