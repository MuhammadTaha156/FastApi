from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base,Session
from fastapi import FastAPI,Depends,HTTPException

app=FastAPI()

#Database URL
DATABASE_URL="sqlite:///./test.db"

#Engine create (DB connection)
engine=create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)

# Session (DB Operation ke liya)
sessionlocal=sessionmaker(autocommit=False, autoflush=False,bind=engine)

# Base (model ka lea)
Base=declarative_base()

# Table (Model)
class Todo(Base):
    __tablename__="todos"

    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    completed=Column(String)

# Tbale Created
Base.metadata.create_all(bind=engine)

# Dependency (DB Session provide kr ra ga)
def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()

# Create API
@app.post("/todos")
def create_todo(title:str,db:Session=Depends(get_db)):
    todo=Todo(title=title,completed="False")
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return{
        "message":"Todo Created",
        "data":todo
    }
   
# Read all Data
@app.get("/todos")
def get_todos(db:Session=Depends(get_db)):
    todos=db.query(Todo).all()
    return {"Total":len(todos),
           "data":todos
           }

# Read filer one
@app.get("/todos/{todo_id}")
def get_todo(todo_id:int,db:Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id==todo_id).first()

    if not todo:
        raise HTTPException(status_code=404,details="Todo not found")
    return todo

# Update Data
@app.put("/todos/{todo_id}")
def update_todo(todo_id:int,title:str,db:Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id==todo_id).first()
    if not todo:
            raise HTTPException(status_code=404,details="Todo not found")
    todo.title=title
    db.commit()
    db.refresh(todo)
    return{
        "message":"Todo Updated",
        "Data":todo
    }

# Delete API
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")  # fixed

    db.delete(todo)
    db.commit()

    return {"message": "TODO Deleted"}






