## Servlet Container
* FastAPI introduces this new concept
* Removes traditiional 'play/start' button 
* Requires FastAPI 

## FastAPI
' Install: $ uv pip install "fastapi[standard]"
* Verify instalation through .venv package 
    * uv pip list or uv pip show fastapi
* Start APP: $ fastapi dev FILENAME.py
    * IMPORTANT: stand in the same folder as main.py

## EndPoint 
* API & URL related 
* Consists of a path : "/example"
* Accompanied by an HTTP-Method (GET, POST, PUT, DELETE)

## Decorator 
* Refers to the @ symobl 
* (Differnce in how function executes)
* Runs logic from external decorator function
    * function over function 
* Returns JSON data (automaic conversion)

```python
@decorator 
def test_function():
```

## URL

Example URL: # 