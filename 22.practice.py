#12. Given a number, check if it’s positive, negative, or zero.
num=int(input("Enter a number: "))
if num<0:
    print("Given Number is negative")
elif num==0:
    print("Given Number is Zero")
elif num>0:
    print("Given Number is Positive")
else:
    print("Invalid Input!..")
        