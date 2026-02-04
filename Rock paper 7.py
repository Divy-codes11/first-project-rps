import random

choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Enter rock, paper or scissors (or q to quit): ").lower()

    if user_choice == "q":
        print("Game over")
        break

    if user_choice not in choices:
        print("Invalid choice")
        continue

    computer_choice = random.choice(choices)

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie")

    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("You win, rock beats scissors")
        else:
            print("You lose, paper beats rock")

    elif user_choice == "paper":
        if computer_choice == "rock":
            print("You win, paper beats rock")
        else:
            print("You lose, scissors beats paper")

    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("You win, scissors beats paper")
        else:
            print("You lose, rock beats scissors")
    if input("Play again? (yes/no): ").lower() != "yes":
        break