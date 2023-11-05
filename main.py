from fastapi import FastAPI
from fastapi_scraper import FastApiScraper
from post_template import PostTemplate
from datetime import datetime

app = FastAPI()

@app.get("/")
async def root():
    replace_tags_file()

    return {"message": "Hello World"}

def create_file(template: list[str]):
    my_string = ' '.join(template)

    with open('post.mdx', 'w', errors='ignore') as file:
        file.write(my_string)

def replace_tags_file():
    fastApiScraper = FastApiScraper()
    scraper_schema = fastApiScraper.scrap()
    template = PostTemplate().get_template()
    body_result_string = ''.join(element.get_text() for element in scraper_schema.body)
    date = get_date()

    for i in range(len(template)):
        template[i] = template[i].replace("body_version", body_result_string)
        template[i] = template[i].replace("title_version", scraper_schema.title)
        template[i] = template[i].replace("date_now", date)

    create_file(template)

def get_date():
    current_datetime = datetime.now()
    date_string = current_datetime.strftime("%Y-%m-%d")
    print(date_string)

    return date_string
