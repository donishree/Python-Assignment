# Electricity Bill Generator

name = input("Enter Consumer Name: ")
consumer_id = input("Enter Consumer ID: ")

previous = float(input("Enter Previous Meter Reading: "))
current = float(input("Enter Current Meter Reading: "))
cost = float(input("Enter Cost per Unit: "))

units = current - previous
energy = units * cost
duty = energy * 0.05
fixed = 100
bill = energy + duty + fixed

print("\n------ ELECTRICITY BILL ------")
print(f"Consumer Name : {name}")
print(f"Consumer ID   : {consumer_id}")
print(f"Units Used    : {units}")
print(f"Energy Charge : ₹{energy:.2f}")
print(f"Duty (5%)     : ₹{duty:.2f}")
print(f"Fixed Charge  : ₹{fixed}")
print(f"Net Bill      : ₹{bill:.2f}")