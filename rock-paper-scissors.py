import random

print("Let's play Rock Paper Scissors! \nType 'r' for rock 'p' for paper and 's' for scissors!")

input = input()

if input == "r":
  player_choice = 1
  print("You chose rock!")
elif input == "p":
  player_choice = 2
  print("You chose paper!")
elif input == "s":
  player_choice = 3
  print("You chose scissors!")

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
