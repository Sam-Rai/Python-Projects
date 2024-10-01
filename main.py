import random

game_images = ["rock", "paper", "scissors"]

user_choice = int(input("What do you chose? Type 0 for Rock, 1 for Paper, or 2 for Scissor."))

computer_choice = random.randint(0, 2)

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("Your win")
elif computer_choice == user_choice:
    print("It's a draw")