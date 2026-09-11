## Input we need from the user
# Total rent
# Total food ordered for snacking
# Electricity units spend
# Charge per unit
# Persons living in room or flat

## Output
# Total amount you've to pay is

rent = int(input("Enter the total rent amount = "))
food = int(input("Enter the amount of food ordered = "))
electricity_units = int(input("Enter the electricity units spent = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of persons living in the room or flat = "))

total_bill = electricity_units * charge_per_unit

output = (food + rent + total_bill) // persons

print("Each person will pay = ", output)

