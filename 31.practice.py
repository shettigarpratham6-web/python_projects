"""21. Input total bill & apply discount logic:

1000 → 20% off

500 → 10% off

else → no discount"""
total_bill=float(input("Enter the total amount: "))
if total_bill>=1000:
    disc=total_bill-((20*total_bill)/100)
    print(f"After 20% Discount amount = {disc}")
elif total_bill>=500:
    disc=total_bill-((10*total_bill)/100)
    print(f"After 10% Discount amount = {disc}")
else:
    print("No Discount")