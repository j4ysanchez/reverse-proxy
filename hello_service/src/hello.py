# filepath: /Users/jsanchez/dev/reverse-proxy/hello_service/src/hello.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/hello/{name}")
def read_hello(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/hello_table")
def read_hello_table():
    users = {
        1: {
            'id': 1,
            'name': 'John Doe',
            'email': 'john.doe@example.com'
        },
        2: {
            'id': 2,
            'name': 'Jane Smith',
            'email': 'jane.smith@example.com'
        },
        3: {
            'id': 3,
            'name': 'Alice Johnson',
            'email': 'alice.johnson@example.com'
        }
    }
    return users
    