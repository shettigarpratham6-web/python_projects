#14. Write a program to check if a year is leap year or not.
year=int(input("Enter a Year: "))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(f"Given year {year} is a leap Year")
else:
    print(f"Given year {year} is not a leap year")     