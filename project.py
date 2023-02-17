
print("Введите год")
year = int(input())


def sum_of_date(year):
    
    total = 0

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        leap_year = True
    else:
        leap_year = False

    for month in range(1, 13):

        if month in [1, 3, 5, 7, 8, 10, 12]:
            days = 31

        elif month in [4 ,6 ,9 ,11]:
            days = 30

        else:
            if leap_year:
                days = 29

            else:
                days = 28 

        for day in range(1 ,days + 1):

            total += sum([int(x) for x in str(day)])

    return total

print(sum_of_date(year))