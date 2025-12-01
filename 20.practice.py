#10. Swap two numbers without using a third variable.
num1=int(input("Enter the value of A: "))
num2=int(input("Enter the value of B: "))
print("Before Swapping Two values:\n")
print("A:",num1)
print("B:",num2)
print("After Swapping Two values:\n")
temp=num1
num1=num2
num2=temp
print("A:",num1)
print("B:",num2)
