import art
import random



EASY_LEVEL = 10
HARD_LEVEL = 5


def check_answer(user_guess, actual_answer, lives):
    if user_guess > actual_answer:
        print("Too high.")
        return lives-1
    elif user_guess < actual_answer:
        print("Too low.")
        return lives-1
    else:
        print(f"You got it! The answer was {user_guess}")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL





def game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    random_number = random.randint(1, 100)
    print(f"The correct asnwer is: {random_number}")

    # your_choice = input("Choose a difficult. Type 'easy' or 'hard':").lower()

    lives = set_difficulty()
   

    guess = 0

    while guess != random_number:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        lives = check_answer(guess, random_number, lives)

        if lives == 0:
            print("You are out off lives. You loss.")
            return
        elif lives != 0:
            print("Guess again.")

game()

while input("Do you want to play again. Type 'yes' or 'no'").lower() == "yes":
    print("\n" * 20)
    game()