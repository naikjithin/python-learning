# Bill calculator program

# We're going to build a tip calculator.
#
# If the bill was $150.00, split between 5 people, with 12% tip.
#
# Each person should pay:
#
# (150.00 / 5) * 1.12 = 33.6
#
# After formatting the result to 2 decimal places = 33.60

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
bill_tip = float(bill * tip / 100)
total_bill = bill + bill_tip
people = int(input("How many people to split the bill? "))
bill_per_person = total_bill / people
print(f"Total amount payable per person is {bill_per_person}")

# output
# Welcome to the tip calculator!
# What was the total bill? $100
# What percentage tip would you like to give? 10 12 15 10
# How many people to split the bill? 2
# Total amount payable per person is 55.0