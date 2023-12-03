from datetime import datetime
import re

def get_date():
    current_datetime = datetime.now()
    formatted_date = current_datetime.strftime("%B %d, %Y")

    return formatted_date

def remove_html_special_characters(line: str):
    pattern = r'[^a-zA-Z0-9\.\s]'

    return re.sub(pattern, '', line)