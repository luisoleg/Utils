# Return the a number representing the number of days of the leap years in the period provided. 
# Those days are not considered if the start date is after 29th of february or the end date is
# before. 
def get_leap_days(start_date, end_date):
    leap_days = 0
    start_year = get_rounddown_year(start_date)
    end_year = get_rounddown_year(end_date)
    period = range(end_year - start_year + 1)

    current_year = start_year
    
    for year in period:
        leap_days = leap_days + 1 if is_leap_year(current_year) else leap_days
        current_year = current_year + 1
    return leap_days

# Based on the leap year rules return true if the given year is considered leap year otherwise
# return false
def is_leap_year(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Determines if the given date is before the possible leap day
def is_before_leap_day(date):
    if(date.month > 2):
        return False
    return True


# Round down the given year looking for a possible leap day
def get_rounddown_year(date):
    year = date.year
    if(is_before_leap_day(date)):
        year = year - 1
    return year
