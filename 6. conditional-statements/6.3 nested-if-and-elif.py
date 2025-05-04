print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("Enter the age of the person? "))
    if age <= 12:
        print("You need to pay $5")
    elif age <=18:
        print("You need to pay $8")
    else:
        print("You need to pay 12$")
else:
    print("Sorry you have to grow taller before you can ride.")

# output
# Welcome to the rollercoaster!
# What is your height in cm? 170
# You can ride the rollercoaster
# Enter the age of the person? 12
# You need to pay $5