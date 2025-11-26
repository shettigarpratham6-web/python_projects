#Truth table for OR Gate

print("Truth Table For OR Gate:(Two Variable) ")
print("\n\n")
a = True
b = False
# In terms of True and False
print("True   or  False: ",a or b)
print("True   or  True : ",a or a)
print("False  or  True : ",b or a)
print("False  or  False: ",b or b)

#In terms of 0's and 1's
print("\n\n")

print("1   or   0: ",int(a or b))
print("1   or   1: ",int(a or a))
print("0   or   1: ",int(b or a))
print("0   or   0: ",int(b or b))