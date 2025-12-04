#16. Input age; check if a person is eligible to vote (>17).
name=input("Enter the name: ")
age=int(input("Enter the Age: "))
if age>17:
    print(f"{name} is Eligible to vote")
else:
    print(f"{name} is not eligible to vote")