# find days in a year

# Type 1
print('####Type_1#####')
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def leap_year(year):
    return year % 4 == 0 and (year != 100 or year != 400)

def days_in_month(year, month):
    if not 1 < month < 12:
        print('Invalid month')
    elif leap_year(year) and month == 2:
        print('29')
    else:
        print(month_days[month])

days_in_month(2017,2)


# Type 2
print('####Type_2#####')

month_days_2 = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def leap_year_2(year):
    return year % 4 == 0 and (year != 100 or year != 400)

def days_in_month_2(year, month):
    if not 1 <= month <= 12:
        return 'Invalid month'
    elif leap_year_2(year) and month == 2:
        return('29')
    else:
        return(month_days_2[month])

print(days_in_month_2(2020,2))
print(days_in_month_2(2020,0))
