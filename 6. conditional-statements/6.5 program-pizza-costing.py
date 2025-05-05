# Pizza costing

# you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.
#
# Based on a user's order, work out their final bill. Use the input() function to get a user's preferences and then add up the total for their order and tell them how much they have to pay.
#
# Small pizza (S): $15
#
# Medium pizza (M): $20
#
# Large pizza (L): $25
#
# Add pepperoni for small pizza (Y or N): +$2
#
# Add pepperoni for medium or large pizza (Y or N): +$3
#
# Add extra cheese for any size pizza (Y or N): +$1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill_amount = 0
if size == 'S':
    bill_amount += 15
    if pepperoni == 'Y':
        bill_amount += 2
elif size == 'M':
    bill_amount += 20
    if pepperoni == 'Y':
        bill_amount += 3
elif size == 'L':
    bill_amount += 25
    if pepperoni == 'Y':
        bill_amount += 3
if extra_cheese == 'Y':
    bill_amount += 1
print(f"Your final bill is: ${bill_amount}.")

# output
# Welcome to Python Pizza Deliveries!
# What size pizza do you want? S, M or L: S
# Do you want pepperoni on your pizza? Y or N: Y
# Do you want extra cheese? Y or N: Y
# Your final bill is: $18.