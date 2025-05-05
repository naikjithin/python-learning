# Rock Paper Scissors
import random
print("Welcome to the stone,paper,scissor game !")
print("Press 0 for stone, 1 for paper and 2 for scissor")

# Rock
print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

choice = int(input("Choose your yours? "))
random_choice = random.randint(0,2)
if choice == 0:
    print("""
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            """)
elif choice == 1:
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
else:
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

print(f"Compute Choice is {random_choice}")

if random_choice == 0:
    print("""
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            """)
elif random_choice == 1:
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
else:
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

if choice == random_choice:
    print("You Win !!!")
else:
    print("You Lose :) Better luck next time !")

# output
# Welcome to the stone, paper, scissor game!
# Press 0 for stone, 1 for paper and 2 for scissor
#
# _______
# ---'   ____)
# (_____)
# (_____)
# (____)
# ---.__(___)
#
# _______
# ---'    ____)____
# ______)
# _______)
# _______)
# ---.__________)
#
#
# _______
# - --'   ____)____
# ______)
# __________)
# (____)
# - --.__(___)
#
# Choose
# your
# yours? 2
#
# _______
# - --'   ____)____
# ______)
# __________)
# (____)
# - --.__(___)
#
# Compute
# Choice is 1
#
# _______
# - --'    ____)____
# ______)
# _______)
# _______)
# ---.__________)
#
# You Lose:) Better luck next time!