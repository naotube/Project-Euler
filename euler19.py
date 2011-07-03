START_YEAR = 1901
END_YEAR = 2000
days_of_months = [31,28,31,30,31,30,31,31,30,31,30,31]

if __name__ == "__main__":
    day_of_week = 1 + 365
    Sundays = 0
    for year in range(START_YEAR, END_YEAR+1):
        for month in range(12):
            if day_of_week % 7 == 0:
                Sundays += 1
            day_of_week = (day_of_week + days_of_months[month]) % 7
            if month == 1:
                if year % 4 == 0:
                    day_of_week += 1
                if year % 100 == 0:
                    if not year % 400 == 0:
                        day_of_week -= 1
    print(Sundays)
