#19. Take a username and password and verify login.
print("--------------------User login Verification-------------------------")
username=input("Enter the User Name: ")
password=input("Enter the Password: ")
print("--------------------confirm username and password-------------------")
username1=input("Enter the User Name: ")
password1=input("Enter the Password: ")
if (username==username1 and password==password1):
    print("Login Confirmed.....!")
else:
    print("Login Failed.....!")
    
