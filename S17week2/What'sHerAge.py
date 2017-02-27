from datetime import date,datetime
def get_age(birth_date,current_date=datetime.utcnow().date()):
    if((current_date.month>birth_date.month) or (current_date.month==birth_date.month and current_date.day>=birth_date.day)):
       return current_date.year-birth_date.year
    return current_date.year-birth_date.year-1