number=int(input("Enter a number: "))
while(number!=0):
    rem=number % 10
    number=number // 10
    print(rem,end="")