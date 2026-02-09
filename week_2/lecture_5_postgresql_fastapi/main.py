from fastapi import FastAPI, status 
from psycopg_pool import ConnectionPool
from psycopg.types.json import Json
from psycopg import Connection

from schema.product import ProductSchema

# This is a connection between the PostgreSQL and the Database (pgadmin).
DATABASE_URL = "postgresql://postgres:My?Psql0228!@localhost:5432/lecture_5"
# ConnectionPool used to connect postgreSQL with Database (pgadmin)
pool = ConnectionPool(DATABASE_URL)
app = FastAPI(title="lecture_5_postgresql_fastapi")

# getter 
@app.get("/")
def root() -> dict:
    return {"Hello": "world"}

@app.post(
        "/products", 
        status_code=status.HTTP_201_CREATED, # Swagger dicumentation clarity 
        response_model=ProductSchema # Swagger documentation update 
    ) 
def post_product(product: ProductSchema) -> ProductSchema:

    # Query-insert 
    with pool.connection() as conn:
        insert_product(conn, product.model_dump())
        conn.commit()

    return product 

# Helper method for DB-queries 
def insert_product(conn: Connection, product: ProductSchema):
    conn.execute(
        "INSERT INTO products_raw (product) VALUES (%s)",
        (Json(product),) 
    )