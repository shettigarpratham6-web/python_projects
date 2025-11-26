# Write a program to swap two variables (without using a third variable).
first_val = int(input("Enter the value of a: "))
second_val = int(input("Enter the value of b: "))
print(f"Before Swapping the Value : a = {first_val} and b = {second_val}")
temp = first_val
first_val = second_val
second_val = temp
print(f"After Swapping the Value : a = {first_val} and b = {second_val}")