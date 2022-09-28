import random

print("this is a rock paper scissors game. \nPick your option then the computer will throw out its choice")
player_choice = input("Rock, Paper or Scissors? (Non case-sensitive) ")
chosen_number = 0
if player_choice.lower() == "rock":
    chosen_number = 1
elif player_choice.lower() == "paper":
    chosen_number = 2
elif player_choice.lower() == "scissors":
    chosen_number = 3
else:
    print("This is not an option, game will now end")
    quit()

computer_choice_number = random.randint(1,3)

if computer_choice_number == 1:
    print("Computer has chosen Rock")
elif computer_choice_number == 2:
    print("Computer has chosen Paper")
elif computer_choice_number == 3:
    print("Computer has chosen Scissors")

if computer_choice_number == chosen_number:
    print("Its a tie! Try again")
elif chosen_number == 1 and computer_choice_number == 2:
    print("Computer Wins!")
elif chosen_number == 1 and computer_choice_number == 3:
    print("You Win!")
elif chosen_number == 2 and computer_choice_number == 1:
    print("You Win!")
elif chosen_number == 2 and computer_choice_number == 3:
    print("Computer Wins!")
elif chosen_number == 3 and computer_choice_number == 1:
    print("Computer Wins!")
elif chosen_number == 3 and computer_choice_number == 2:
    print("You Win!")

