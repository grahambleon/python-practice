import random

print("Let's play Rock Paper Scissors! \nType 'r' for rock 'p' for paper and 's' for scissors!")

def get_user_input():
    player_input = input()
    if player_input == "r":
        print("You chose rock!")
        return 1
    elif player_input == "p":
        print("You chose paper!")
        return 2
    elif player_input == "s":
        print("You chose scissors!")
        return 3
    else:
        print("Invalid choice!  Try again.")
        get_user_input()

player_choice = get_user_input()
computer_choice = random.randint(1,3)

if computer_choice == 1:
    print("Computer chose rock!")
elif computer_choice == 2:
    print("Computer chose paper!")
elif computer_choice == 3:
    print("Computer chose scissors!")

if player_choice == computer_choice:
    print("It's a tie!")
elif player_choice == 1 and computer_choice == 2:
    print("Computer wins!")
elif player_choice == 1 and computer_choice == 3:
    print("You win!")
elif player_choice == 2 and computer_choice == 1:
    print("You win!")
elif player_choice == 2 and computer_choice == 3:
    print("Computer wins!")
elif player_choice == 3 and computer_choice == 1:
    print("Computer wins!")
elif player_choice == 3 and computer_choice == 2:
    print("You win!")
