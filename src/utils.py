from datetime import datetime

def get_date():
    current_datetime = datetime.now()
    date_string = current_datetime.strftime("%Y-%m-%d")
    print(date_string)

    return date_string