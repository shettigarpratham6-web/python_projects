#Implicit Type Conversion
a = 10
b = 10.562345
c = a + b  #Lower dataType Converted into Higher DataType
print(a,"Its Type: ",type(a))
print(b,"Its Type: ",type(b))
print(c,"Its Type: ",type(c))

#Limitation of Decimal Points using round() function

print("Result with 1 Decimal Point: ",round(c,1))
print("Result with 2 Decimal Points: ",round(c,2))
print("Result with 4 Decimal Points: ",round(c,4))

#Limitation of Decimal Points using Format() function
first_val = 21.34
second_val = 34.56
Result = first_val*second_val
print("Result with 3 Decimal Points: ",format(Result,".3f"))
print("Result with 4 Decimal Points: ",format(Result,".4f"))

#Limitation of Decimal Points using f string function

print(f"Result with 4 Decimal Places: {Result:.4f}")
print(f"Result with 6 Decimal Places: {Result:.6f}")