from fastapi import FastAPI
from scraper.scraper_strategy import Scraper, FastApiScraperStrategy
from file_helper import scraper 

app = FastAPI()

@app.get("/")
def root():
    fastapi_scraper = FastApiScraperStrategy()
    api_scraper = Scraper(fastapi_scraper)
    scraper(api_scraper)
    return {"message": "Hello World"}


