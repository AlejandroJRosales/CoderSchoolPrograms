import random


pc_choices = ["Rock", "Paper", "Scissors"]

iterations = int(input("How many times do you want to play: "))
num_pc_wins = 0
num_usr_wins = 0
for count in range(iterations):
    pc_choice = random.choice(pc_choices)
    usr_choice = input("Rock, Paper, or Scissors: ")

    if pc_choice == "Rock" and usr_choice == "Rock":
        print("Tie!")
        num_pc_wins += .5
        num_usr_wins += .5
    elif pc_choice == "Rock" and usr_choice == "Paper":
        print("You won!")
        num_usr_wins += 1
    elif pc_choice == "Paper" and usr_choice == "Rock":
        print("Computer won!")
        num_pc_wins += 1
    elif pc_choice == "Rock" and usr_choice == "Scissors":
        print("Computer won!")
        num_pc_wins += 1
    elif pc_choice == "Scissors" and usr_choice == "Rock":
        print("You won!")
        num_usr_wins += 1
    elif pc_choice == "Paper" and usr_choice == "Paper":
        print("Tie!")
        num_pc_wins += .5
        num_usr_wins += .5
    elif pc_choice == "Paper" and usr_choice == "Scissors":
        print("You won!")
        num_usr_wins += 1
    elif pc_choice == "Scissors" and usr_choice == "Paper":
        print("Computer won!")
        num_pc_wins += 1
    elif pc_choice == "Scissors" and usr_choice == "Scissors":
        print("Tie!")
        num_pc_wins += .5
        num_usr_wins += .5

    if num_pc_wins < num_usr_wins:
        print("Your winning!")
    elif num_pc_wins > num_usr_wins:
        print("The computer is winning!")
    else:
        print("It's a tie!")
    print("Score:")
    print(f"\tYou: {num_usr_wins}")
    print(f"\tComputer: {num_pc_wins}\n")

if num_pc_wins < num_usr_wins:
    print("You won!")
elif num_pc_wins > num_usr_wins:
    print("Computer won!")
else:
    print("It's a tie!")
