from fastapi import FastAPI

app =FastAPI()

# TODOS=[
#     {
#     'Title':"Task 1","Description":"My Task1","Is_Competed":False},
#     {
#     'Title':"Task 2","Description":"My Task2","Is_Competed":False},
#     {
#     'Title':"Task 3","Description":"My Task3","Is_Competed":False},
#     {
#     'Title':"Task 4","Description":"My Task4","Is_Competed":False},
# ]

@app.get('/')
def home():
    return {"message":"Hello World"}

# @app.get('/todos/all')
# def get_All_todos():
#     return TODOS

