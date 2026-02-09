Postgresql & Fastapi 

Installation 

UV pip install "fastapi[standard]"
UV pip install "psycopg[binary]"
UV pip install "psycopg[pool]"

RUN APP 
$ FastAPI dev main.py  

Storing data philosphy 
Whats the purpose of the data
- Bulk upploading 
- Json data storage 
- Unorganized data 
- PostgreSQL database 

Whats the type of said data?
- Unorganized 
- Unstructured 
- JSON 

DATABASE - PostgreSQL
- A newley created database does not contain any tables by default 

Step #1 - Create a new Table (products)

```postgresql
CREATE TABLE IF NOT EXISTS products_raw(
    id BIGSERIAL PRIMARY KEY,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    product JSONB NOT NULL
);
```

Step #2 - Create a connection with the Database using URL
Assuming you are using pgadmin4 you can find the required data like so: 
* Username: Right-click your own database -> properties -> username
* Passsword: You should know this one, changeable if the server is up and running.
* Port: Right-click PostgreSQL 18 -> porperties -> connection -> port
* Address: Same steps as with port 

```python
DATABASE_URL = "postgresql://postgres:PSW@ADDRESS:PORT/DB_NAME"
```

Step #3 - Implement a function for insert (FastAPI)


```python
def insert_product(conn: Connection, product: ProductSchema):
    conn.execute(
        "INSERT INTO products_raw (product) VALUES (%s)",
        (Json(product),) 
    )
```

Use helper-method
```python
@app.post(
        "/products", 
        status_code=status.HTTP_201_CREATED, # Swagger dicumentation clarity 
        response_model=ProductSchema # Swagger documentation update 
    ) 
def post_product(product: ProductSchema) -> ProductSchema:

    # Query-insert 
    with pool.connection() as conn:
        insert_product(conn, product)
        conn.commit()

    return product 
```

Postman test against `localhost:8000/products`:
```json
{
    "product_id": "USP239",
    "name": "Wireless Mouse",
    "price": 249.0,
    "currency": "SEK",
    "category": "Electronics",
    "brand": null
}
```

When using .toml and uv.lock remember 
Changes made to uv does not update autmatically. 
$ uv add "package-name" is needed to update .toml and uv lock