#20. Check whether a number lies between 100 and 500.
number=int(input("Enter a number: "))
if number>=100 and number<=500:
    print(f"{number} lies between 100 and 500")
else:
    print(f"{number} not lies between 100 and 500")