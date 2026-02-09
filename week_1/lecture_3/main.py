from typing import Union

from fastapi import FastAPI

app = FastAPI(title="My first API APP")

# Function {dictionary with key : pair}
@app.get("/")
def root():
    return {"Hello": "World"}

# # Two endpoints: items and {item_id} 
# @app.get("/items/{item_id}") # localhost:8000/items/249
# # We type out int, incase of an error we get specified feedback
# def get_item(item_id: int): 
#     #Return dictionary: Key : Pair
#     return{"item_id": item_id}

# This example is used to specifie for example a shirt color option on a shopping page.
@app.get("/items/{item_id}") # localhost:8000/items/249?color=blue
# We type out int, incase of an error we get specified feedback
def get_item(item_id: int, color: Union[str, None] = None): # Creates a list 
    #Return dictionary: Key : Pair
    return{"item_id": item_id, "color": color}

