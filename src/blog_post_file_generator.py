from utils import get_date, remove_html_special_characters
from constants import POST_TEMPLATE
from database.redis_client import redis_client
from scraper.scraper_strategy import ScraperContext, FastApiScraperStrategy

def create_file(template, title, scraper_context: ScraperContext):
    my_string = ' '.join(template)
    with open(f'{scraper_context.api_post_directory()}/{title}.mdx', 'w', errors='ignore') as file:
        file.write(my_string)

def scraper():
    scraper_context = get_scraper()
    scraper_schema = format_resulting_scraper(scraper_context)
    existingPost = verify_existing_post(scraper_context.api_description(), scraper_schema.title)
    
    if (existingPost):
        return
        
    template = generate_template(scraper_schema)
    create_file(template, scraper_schema.title, scraper_context)
    redis_client.set(scraper_context.api_description() + scraper_schema.title, scraper_schema.title)
    
def format_resulting_scraper(scraper: ScraperContext):
    scraper_schema = scraper.scraper()
    scraper_schema.title = remove_html_special_characters(scraper_schema.title)
    return scraper_schema

def format_body_result(scraperBody):
    body_result_string = ''.join(element.get_text() for element in scraperBody)
    body_result_string = remove_html_special_characters(body_result_string)
    return body_result_string

def verify_existing_post(apiDescription: str, postTitle: str) -> bool:
    existingPost = redis_client.get(apiDescription + postTitle)
    return existingPost != None

def generate_template(scraper):
    template = POST_TEMPLATE
    body_result_string = format_body_result(scraper.body)
    date = get_date()

    for i in range(len(template)):
        template[i] = template[i].replace("body_version", body_result_string)
        template[i] = template[i].replace("title_version", scraper.title)
        template[i] = template[i].replace("date_now", date)
    
    return template

def get_scraper():
    fastapi_scraper = FastApiScraperStrategy()
    api_scraper = ScraperContext(fastapi_scraper)
    return api_scraper
    