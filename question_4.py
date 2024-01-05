def is_leap_year(year):

    if year % 4 == 0:

        print("this is a leap year!")
    
    elif year % 400 == 0 or year % 100 != 0:

        print("this is not a leap year!")


is_leap_year(2022)