def is_year_leap(year):
    if year < 1582:
        return False
    elif year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    if month > 12 or year < 1582:
        return None
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28


def day_of_year(year, month, day):
    days = 0
    
    for m in range(1, month):
        days += days_in_month(year, m)
    
    result = days + day
    return result

print(day_of_year(2000, 12, 31))
