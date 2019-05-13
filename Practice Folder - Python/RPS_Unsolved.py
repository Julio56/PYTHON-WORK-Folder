# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]
    "r" = Rock
    "p" = Paper
    "s" = Scissors

# Computer Selection
computer_choice = random.choice(options)



# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
if (computer_choice == "r" and user_choice = "s") then print("Computer Wins!")
    elif user_choice = "p" then print("User Win!")
    elif user_choice = "r" then print("It's a Tie!")

if (computer_choice = "p" and user_choice = "s") then print("User Win!")
    elif user_choice = "r" then print("Computer Wins!")
    elif user_choice = "p" then print("It's a Tie!")

if (computer_choice = "s" and user_choice = "r") then print("User Wins!")
    elif user_choice = "p" then print("Computer Wins!")
    elif user_choice = "s" then print("It's a Tie!")