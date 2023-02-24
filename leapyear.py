year=int(input(print("Enter a year: ")))
if year<0:
    print("Invalid Input...")
else:
    if year%400==0:
        print(year,"is a leap year")
    elif year%4==0 :
        print(year,"is a leap year")
    else:
        print(year,"is not a leap year i.e. a normal year")           