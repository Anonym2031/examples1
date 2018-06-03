def season(month):
    if 3 <= month <= 5:
        print("\nSpring")
    elif 5 < month <= 8:
        print("\nSummer")
    elif 8 < month <= 11:
        print("\nAutumn")
    elif month == 12 or month == 1 or month == 2:
        print("\nWinter")
    else:
        print("\nError")


num_of_month = int(input("Input number of month   -  "))
season(num_of_month)
