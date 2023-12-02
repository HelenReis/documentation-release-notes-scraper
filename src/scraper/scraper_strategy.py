from scraper.fastapi_scraper import FastApiScraper
from models import ScrapingSchema

class ScraperStrategy:
    """Class representing a scraper strategy"""
    api_description = 'NONE'
    
    def scraper(self) -> ScrapingSchema:
        pass
    
class FastApiScraperStrategy(ScraperStrategy):
    api_description = 'fastapi'
    
    def scraper(self):
        fastApiScraper = FastApiScraper()
        return fastApiScraper.scrap()
    
class OtherApiScraperStrategy(ScraperStrategy):
    api_description = 'OTHER'
    
    def scraper(self):
        pass
        
class Scraper:
    def __init__(self, scraper_strategy: ScraperStrategy):
        self.scraper_strategy = scraper_strategy
        
    def scraper(self) -> ScrapingSchema:
        return self.scraper_strategy.scraper()
        
    def api_description(self): return self.scraper_strategy.api_description