from fastapi import FastAPI
from fastapi_scraper import FastApiScraper
from post_template import PostTemplate
import re

app = FastAPI()

@app.get("/")
async def root():
    replace_tags_file()

    return {"message": "Hello World"}

def create_file(template: list[str]):
    my_string = ' '.join(template)

    with open('example.mdx', 'w', errors='ignore') as file:
        file.write(my_string)

def replace_tags_file():
    fastApiScraper = FastApiScraper()
    elements_between = fastApiScraper.scrap()
    template = PostTemplate().get_template()
    result_string = ''.join(element.get_text() for element in elements_between)
    print(result_string)

    for i in range(len(template)):
        template[i] = template[i].replace("body_version", result_string)

    create_file(template)