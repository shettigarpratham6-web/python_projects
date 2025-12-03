#15. Check if a number is divisible by both 3 and 7.
num=int(input("Enter a number: "))
if (num % 3 ==0) and (num % 7 ==0):
    print(f"Given Number {num} is Divisible by 3 and 7")
else:
    print(f"Given Number {num} is Not Divisible by 3 and 7")    