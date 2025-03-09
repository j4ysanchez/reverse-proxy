from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Location Service"}

@app.get("/locations")
def get_locations():
    locations = [
        {"city": "Toronto", "country": "Canada"},
        {"city": "Vancouver", "country": "Canada"},
        {"city": "Montreal", "country": "Canada"},
        {"city": "New York", "country": "USA"},
        {"city": "Los Angeles", "country": "USA"}
    ]
    return locations