def leap_year(year):
    if year % 4 is 0 and year % 100 is not 0:
        return True
    elif year % 400 is 0:
        return True
    else:
        return False
