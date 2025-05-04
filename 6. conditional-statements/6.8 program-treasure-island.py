# Treasure island project

# Your goal today is to build a "Chose your own adventure game". Using what you have learnt in the lessons today you will be building a very simple version of this type of text game.
#
# Use the flow chart linked here to create the game logic.
#
# Once you've completed the project, you can always extend the game and make it more interesting!

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/_¯¯¯ˀˀ¯ˀˀˀ¥¥¥¥¥¥_____/______/______/_____ /
******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("Which direction - left or right or anything else?? ").lower()

if direction == "left":
    option = input("Do you want to swim or wait? ").lower()
    if option == "wait":
        door = input("Which door - Red or Blue or Yellow or Anything ?").lower()
        if door == "Red":
            print("Burned by fire. Game over !!")
        elif door == "Blue":
            print("Eaten by beasts. Game over !!")
        elif door == "Yellow":
            print("You Win!")
        else:
            print("Game Over !!")
    else:
        print("Fall into a hole. Game over !!!")
else:
    print("Fall into a hole. Game over !!!")

#ouput
# Welcome to Treasure Island.
# Your mission is to find the treasure.
# Which direction - left or right or anything else?? left
# Do you want to swim or wait? swim
# Fall into a hole. Game over !!!