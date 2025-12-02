#13. Check if a number is divisible by 5.
number=int(input("Enter a Number: "))
if number%5==0:
    print(f"The Given Number {number} is divisible by 5 ")
elif number%5!=0:
    print(f"The Given Number {number} is not divisible by 5 ")
else:
    print("Invalid Input!..")    
        