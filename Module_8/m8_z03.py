from datetime import datetime

date = '2021-05-27 17:08:34.149Z'


def get_str_date(date):

    date_time = date.split(' ')
    dete_date = date_time[0].split('-')
    this_day = datetime(int(dete_date[0]), int(
        dete_date[1]), int(dete_date[2]))
    # print(this_day.strftime('%A %d %B %Y'))
    return this_day.strftime('%A %d %B %Y')


get_str_date(date)
