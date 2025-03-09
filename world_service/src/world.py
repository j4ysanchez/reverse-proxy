# filepath: /Users/jsanchez/dev/reverse-proxy/hello_service/src/hello.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "New service, who dis?"}

@app.get("/world/{name}")
def read_hello(name: str):
    return {"message": f"Bello, {name}!"}