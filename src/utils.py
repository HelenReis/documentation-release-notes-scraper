from datetime import datetime
import re

def get_date():
    current_datetime = datetime.now()
    date_string = current_datetime.strftime("%Y-%m-%d")
    print(date_string)

    return date_string

def remove_html_special_characters(line: str):
    pattern = r'[^a-zA-Z0-9\.\s]'

    return re.sub(pattern, '', line)