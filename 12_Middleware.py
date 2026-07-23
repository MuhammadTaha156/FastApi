from fastapi import FastAPI,status,HTTPException,Request,Depends,Header,middleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import time

app=FastAPI()


# @app.middleware("https")
# async def my_middleware(request:Request,call_next):
#     print("Request Received")

#     response=await call_next(request)
#     print("Response Sent")

#     return response


@app.middleware("https")
async def my_middleware(request:Request,call_next):
    start_Time=time.time()
    print("Request Received")

    response=await call_next(request)

    process_time=time.time()-start_Time
    print(f"Path:{request.url.path} | Time: {process_time}")
    print("Response Sent")

    return response




    