from datetime import datetime

date = '2021-10-09'


def get_days_from_today(date):


    current_date = datetime.now()
    
    date = date.split('-')

    user_date = datetime(year=int(date[0]), month=int(date[1]),day=int(date[2]))

    return  (current_date - user_date).days
    
    
    
    
print(get_days_from_today(date))