import random


pc_choices = ["Rock", "Paper", "Scissors"]
pc_choice = random.choice(pc_choices)
usr_choice = input("Rock, Paper, or Scissors: ")

if pc_choice == "Rock" and usr_choice == "Rock":
    print("Tie!")
elif pc_choice == "Rock" and usr_choice == "Paper":
    print("You win!")
elif pc_choice == "Paper" and usr_choice == "Rock":
    print("Computer win!")
elif pc_choice == "Rock" and usr_choice == "Scissors":
    print("Computer wins!")
elif pc_choice == "Scissors" and usr_choice == "Rock":
    print("You win!")
elif pc_choice == "Paper" and usr_choice == "Paper":
    print("Tie!")
elif pc_choice == "Paper" and usr_choice == "Scissors":
    print("You win!")
elif pc_choice == "Scissors" and usr_choice == "Paper":
    print("Computer wins!")
elif pc_choice == "Scissors" and usr_choice == "Scissors":
    print("Tie!")
