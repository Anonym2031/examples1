def bank(m, y):
    for i in range(y):
        m = m + m*y/100
    print(m)


money = int(input("Input Money -  "))
years = int(input("\nInput Years -  "))
bank(money, years)
