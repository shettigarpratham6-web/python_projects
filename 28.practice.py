#18. Input temperature and classify: Hot, Warm, Cold.
temperature=float(input("Enter the Temperature: "))
if temperature>30:
    print("Its HOT")
elif (temperature>=15 and temperature<=30):
    print("Its Warm")
elif temperature<15:
    print("Its Cold")
