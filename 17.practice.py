#7. Convert boolean True into integer.
value=input("Enter a Boolean Value: ")
if value.lower()=="true":
    print(int(True))
elif value.lower()=="false":
    print(int(False))
else:
    print("Invalid Input!,try Again..")        