from bs4 import NavigableString
from typing import List

class ScrapingSchema:
  def __init__(self, title, body):
        self.title = title
        self.body = body

  title: str = ""
  body: List[NavigableString] = []