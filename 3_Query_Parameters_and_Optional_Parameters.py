from fastapi import FastAPI

app=FastAPI()


#Optional Parameters
@app.get("/users")
def get_users(name: str=None):
    return {"Name":name}

#Default Parameters values
@app.get("/products")
def get_limit(limit: int=10):
    return {"Limit":limit}

#Multiple Query Parameters
@app.get("/items")
def get_items(name: str=None, price: int=0):
    return {"Item":name,
            "Price":price} 


