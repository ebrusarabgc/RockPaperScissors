import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_score = 0
computer_score = 0

images = [rock, paper, scissors]

while user_score < 3 and computer_score < 3:
    rock_paper_scissors = input("Rock, paper or scissors? ")
    rock_paper_scissors = rock_paper_scissors.lower()
    # So even though it is written in different ways (like ROCK, rock and Rock), it will be treated in the same way.

    computer_choice = random.randint(0, 2)
    # 0 --> rock, 1 --> paper, 2 --> scissors
    user_choice = -1

    if rock_paper_scissors == "rock":
        user_choice = 0
    elif rock_paper_scissors == "paper":
        user_choice = 1
    elif rock_paper_scissors == "scissors":
        user_choice = 2

    show_user_choice = images[user_choice]
    show_computer_choice = images[computer_choice]

    if user_choice == -1:
        show_user_choice = "\nInvalid choice.\n"

    print(f"\nYou: \n {show_user_choice} \nMe: \n {show_computer_choice}")

    if (user_choice == 0 and computer_choice == 2) or user_choice > computer_choice:
        print("You win.")
        user_score += 1
    elif user_choice == computer_choice:
        print("It's a draw.")
    else:
        print("You lose.")
        computer_score += 1

    print(f"Your Score = {user_score} | My Score = {computer_score}")

if user_score == 3:
    print("You won the game...")
else:
    print("You lose the game!")
