from fastapi import FastAPI

app=FastAPI()

#Home Route
@app.get("/")
def home():
    return {"message":"Welcome to Fastapi"}


#About Route
@app.get("/about")
def about():
    return {"message":"This is about page"}

#Users Route
@app.get("/users")
def Users():
    return {"users":["Taha","Hanzala"]}




