# Mathematical Calculator using Built-in Functions and Math Module

import math

num = float(input("Enter a number: "))

print("\n------ RESULTS ------")
print("Square        :", num ** 2)
print("Cube          :", num ** 3)
print("Square Root   :", math.sqrt(num))
print("Ceiling Value :", math.ceil(num))
print("Floor Value   :", math.floor(num))
print("Absolute Value:", abs(num))
print("Type          :", type(num))
print("Memory Address:", id(num))