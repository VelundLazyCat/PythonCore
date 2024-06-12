from datetime import date
month = 12
year = 2021


def get_days_in_month(month, year):

    current_month = date(year, month, 1)
    if month == 12:
        next_month = date(year+1, 1, 1)
    else:
        next_month = date(year, month+1, 1)
    result = abs(next_month - current_month)

    return result.days


print(get_days_in_month(month, year))
