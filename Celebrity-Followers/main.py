import art
from game_data import data
import random

random_data1 = random.choice(data)
count = 0
in_game = True
print(art.logo)

while in_game:


    random_data2 = random.choice(data)

    def correct_answer():
        if random_data1["follower_count"] > random_data2["follower_count"]:
            return "A"
        else:
            return "B"

    print(f"Compare A: {random_data1["name"]},a {random_data1["description"]}, from {random_data1["country"]}")
    print(art.vs)
    print(f"Against B: {random_data2["name"]},a {random_data2["description"]}, from {random_data2["country"]}")
    user_ans = input("Who has more followers? Type 'A' or 'B': ").upper()
    print("\n" * 20)

    if user_ans == correct_answer():
        count += 1
        print(art.logo)
        print(f"You're right! Current score: {count}.")
        random_data1 = random_data2
    else:
        in_game = False
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {count}.")
        count = 0
