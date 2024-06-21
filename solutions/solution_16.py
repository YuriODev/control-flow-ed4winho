def next_date(day, month, year):
    if month == 2:
        if day == 29 and (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0)):
            day = 1
            month = 3
        else:
            day += 1
    elif month in [4, 6, 9, 11]:
        if day < 30:
            day += 1
        else:
            day = 1
            month += 1
    else:  # month == 1 (January), month == 3 (March), month == 5 (May), month == 7 (July), month == 8 (August), month == 10 (October), month == 12 (December)
        if day < 31:
            day += 1
        else:
            day = 1
            if month < 12:
                month += 1
            else:
                month = 1
                year += 1

    return f"{day}.{month}.{year}"

day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

print(next_date(day, month, year))
