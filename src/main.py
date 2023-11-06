from fastapi import FastAPI
from file_helper import replace_tags_file 


app = FastAPI()

@app.get("/")
async def root():
    replace_tags_file()

    return {"message": "Hello World"}


