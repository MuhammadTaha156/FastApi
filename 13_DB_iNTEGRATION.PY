from fastapi import FastAPI,status,HTTPException,Request,Depends,Header,middleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import time
import sqlite3

app=FastAPI()

conn=sqlite3.connect("test.db",check_same_thread=False)


cursor=conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS todos(
                                                id INTEGER PRIMARY KEY,
                                                title TEXT,
                                                completed Text
                                            )
""")

conn.commit()

@app.get("/")
def home():
    return{
        "message":"SQLite Connected fine"
    }






