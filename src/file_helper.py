from scraper.fastapi_scraper import FastApiScraper
from utils import get_date
from constants import POST_TEMPLATE

def create_file(template: list[str]):
    my_string = ' '.join(template)

    with open('blog_posts/post.mdx', 'w', errors='ignore') as file:
        file.write(my_string)

def replace_tags_file():
    fastApiScraper = FastApiScraper()
    scraper_schema = fastApiScraper.scrap()
    template = POST_TEMPLATE
    body_result_string = ''.join(element.get_text() for element in scraper_schema.body)
    date = get_date()

    for i in range(len(template)):
        template[i] = template[i].replace("body_version", body_result_string)
        template[i] = template[i].replace("title_version", scraper_schema.title)
        template[i] = template[i].replace("date_now", date)

    create_file(template)