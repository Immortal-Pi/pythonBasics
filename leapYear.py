# logic to find the leap year using functions
def leapYear(year):

    if year%400==0 or (year % 100==0 and year % 4==0):
        return True
    else:
        return False
