import math
a = math.pi 
b = math.e
print(f"The value of PI is : {a} ")
print(f"The value of e is : {b} ")

x = int(input("Enter the value: "))
print(f"The Square Root of {x} is {math.sqrt(x)}")

print(f"Before round() function: {a}")
a=round(a)
print(f"After round() function: {a}")

print(f"Before round() function: {b}")
b=round(b)
print(f"After round() function: {b}")

print(f"Before ceil() function: {a}")
a=math.ceil(a)
print(f"After ceil() function: {a}")

print(f"Before ceil() function: {b}")
b=math.ceil(b)
print(f"After ceil() function: {b}")

print(f"Before floor() function: {a}")
a=math.floor(a)
print(f"After floor() function: {a}")

print(f"Before floor() function: {b}")
b=math.floor(b)
print(f"After floor() function: {b}")