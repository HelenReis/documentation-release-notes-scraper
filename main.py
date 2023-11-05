from fastapi import FastAPI
from fastapi_scraper import FastApiScraper
from post_template import PostTemplate

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

    for i in range(len(template)):
        template[i] = template[i].replace("body_version", body_result_string)
        template[i] = template[i].replace("title_version", scraper_schema.title)

    create_file(template)