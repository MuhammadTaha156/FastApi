from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

todos=[]

class Todo(BaseModel):
    id:int
    title:str
    completed:bool

@app.post("/todos")
def create_todos(todo:Todo):
    todos.append(todo)
    return {"message":"Todo Added","data":todo}


@app.get('/todos')
def get_todos():
    return todos

@app.get("/todos/{todo_id}")
def get_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
        
    return {"error":"Todo not found"}


@app.post("/todos/{todo_id}")
def update_todo(todo_id:int,updated_todo:Todo):
    for index,todo in enumerate(todos):
        if todo.id==todo_id:
            todos[index]=updated_todo
            return {
                "message":"Data Updated",
                "Data":updated_todo
            }
    return {"Error":"Todo not Found"}
             