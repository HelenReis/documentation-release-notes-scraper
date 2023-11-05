import requests
from bs4 import BeautifulSoup, NavigableString
from scraping_schema import ScrapingSchema
from typing import List
import re

class FastApiScraper:
    def scrap(self):
        page = requests.get('https://fastapi.tiangolo.com/release-notes/')
        soup = BeautifulSoup(page.text, 'html.parser')
        version_regex = re.compile("^\d{5}$")
        last_version = soup.find(id=version_regex)
        last_version_limiter = last_version.find_next(id=version_regex)
        elements_between = self.elements_between_tags(last_version, last_version_limiter)
        result_scraper = ScrapingSchema(last_version.get_text(), elements_between)

        return result_scraper
        

    def elements_between_tags(self, tag1: NavigableString, tag2: NavigableString) -> List[NavigableString]:
        result = []
        current = tag1.find_next()

        while current and current.name != tag2.name:
            if current.name == 'li':
                result.append(current)
            current = current.find_next()

        return result