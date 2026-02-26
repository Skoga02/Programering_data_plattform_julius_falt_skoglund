from fastapi import FastAPI
from starlette import status

from app.schema.Product import ProductSchema

app = FastAPI(title="lecture_9")

@app.get("/")
def root():
    return {"message": "Hello : World"}

@app.post("/products", status_code=status.HTTP_201_CREATED, response_model=ProductSchema)
def post_product(product: ProductSchema) -> ProductSchema:

    return product