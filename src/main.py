from fastapi import FastAPI
from file_helper import scraper

app = FastAPI()

@app.get("/")
def root():
    scraper()
    return {"message": "Hello World"}
