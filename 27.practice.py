#17. Input 3 sides and check if triangle is possible.
a=int(input("Enter the side 1 length: "))
b=int(input("Enter the side 2 length: "))
c=int(input("Enter the side 3 length: "))
if (a+b>c and a+c>b and c+b>a):
    print("It is a Triangle")
else:
    print("It is not a Triangle")    