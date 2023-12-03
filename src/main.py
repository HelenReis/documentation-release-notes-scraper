from fastapi import FastAPI
from blog_post_file_generator import scraper

app = FastAPI()

@app.get("/")
def root():
    scraper()
    return {"message": "Hello World"}
