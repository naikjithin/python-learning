print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill_amount = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill_amount = 5
        print("Please pay $5.")
    elif age <= 18:
        bill_amount = 7
        print("Please pay $7.")
    else:
        bill_amount = 12
        print("Please pay $12.")
    is_photo_required = input("Do you need photo to be taken ? Type y | n")
    if is_photo_required == 'y':
        print("Please pay bill amount + 3$ extra.")
        bill_amount += 3

    print(f"Your total bill to be paid: {bill_amount}$")
else:
    print("Sorry you have to grow taller before you can ride.")

# output
# Welcome to the rollercoaster!
# What is your height in cm?  150
# You can ride the rollercoaster
# What is your age? 18
# Please pay $7.
# Do you need photo to be taken ? Type y | n y
# Your total bill to be paid: 7$