

def main():
    Sunday = 7
    Year = 1900
    Month = 1
    count = 0
    days = 0

    while Year < 2001: # each loop is a week
        
        Sunday += 7
        if (Month == 4, 6, 9, 11):
            days = 30
        elif (Month == 2):
            if (Year % 4 == 0):
                if (Year % 100 == 0 and Year % 400 == 0):
                    days = 29
                elif (Year % 100 == 0 and Year % 400 != 0):
                    days = 28
                else:
                    days = 29
            else:
                days = 28
        else:
            days = 31

        if Sunday > days: # Next month, mod days, check, 
            Sunday = Sunday % days
            Month += 1
            if Sunday == 1:
                if Year > 1900:
                    count += 1
            if Month >= 13: # next year
                Month = 1
                Year += 1


        if Month >= 13: # Next Year
            Month = 1
            Year += 1
    print(count)


if __name__ == "__main__":
    main()
