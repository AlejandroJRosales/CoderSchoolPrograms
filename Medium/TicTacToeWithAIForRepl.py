Tic-Tac-Toe with AI

from random import randint
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)


#Initialising variables for loops
playing = True
playAgain = "y"

player1Wins = 0
player2Wins = 0
player1cpuWins = 0
cpuWins = 0


#spaces aviable in  the gameboard
spaces = ["1,1", "1,2", "1,3", "2,1", "2,2", "2,3", "3,1", "3,2", "3,3"]


#while they want to continue playing (after the've played one game)
while playAgain == "y":

  playing = True

  #clear screen ready for question on play type
  print("\033[2J\033[H")


  #ressetting gameboard after loop
  gameboard = [
  ["   ", " 1 ", " 2 ", " 3 "],
  [" 1 ", "   ", "   ", "   "],
  [" 2 ", "   ", "   ", "   "],
  [" 3 ", "   ", "   ", "   "]
  ]



  #Game mode
  cpu = input("Play against cpu or pvp (cpu/pvp):\n").lower()


  #game mode validation
  while cpu not in ["cpu", "pvp"]:

    print("\033[2J\033[H")
    cpu = input("Invalid.\nPlay against cpu or pvp (cpu/pvp):\n").lower()


  #clears screen for gameboard  
  print("\033[2J\033[H")


  #while the game hasn't ended
  while playing:
    rows = ""

    print("\033[2J\033[H")


    #prints the gameboard
    for row in gameboard:
      for element in row:
        rows+=element
      print(rows)
      rows = ""


    #instructions for pvp mode
    if cpu == "pvp":

      #player 1 choice
      player1 = input(Fore.GREEN + "P1." + Style.RESET_ALL + " Enter square to play (e.g. 1,1 (column, row)):\n").lower()


      #checks for valid input
      while player1 not in spaces or len(player1) != 3 or gameboard[int(player1[-1])][int(player1[0])] != "   ":
        player1 = input("Invalid.\n" + Fore.GREEN + "P1." + Style.RESET_ALL + " Enter square to play (e.g. 1,1 (column, row)):\n")



      #adds player input to the gameboard
      gameboard[int(player1[-1])][int(player1[0])] = Fore.GREEN + " x "

      #clears screen to replace with new updated gameboard
      print("\033[2J\033[H")


      #prints new gameboard
      for row in gameboard:
        for element in row:
          rows+=element
        print(rows)
        rows = ""
          
      

      #Checks if player 1 has won by checking every win posibility for 3 in a row
      if (gameboard[1][1] == Fore.GREEN + " x " and gameboard[1][2] == Fore.GREEN + " x " and gameboard[1][3] == Fore.GREEN + " x ") or (gameboard[1][1] == Fore.GREEN + " x " and gameboard[2][1] == Fore.GREEN + " x " and gameboard[3][1] == Fore.GREEN + " x ") or (gameboard[1][1] == Fore.GREEN + " x " and gameboard[2][2] == Fore.GREEN + " x " and gameboard[3][3] == Fore.GREEN + " x ") or (gameboard[1][2] == Fore.GREEN + " x " and gameboard[2][2] == Fore.GREEN + " x " and gameboard[3][2] == Fore.GREEN + " x ") or (gameboard[1][3] == Fore.GREEN + " x " and gameboard[2][3] == Fore.GREEN + " x " and gameboard[3][3] == Fore.GREEN + " x ") or (gameboard[1][3] == Fore.GREEN + " x " and gameboard[2][2] == Fore.GREEN + " x " and gameboard[3][1] == Fore.GREEN + " x ") or (gameboard[2][1] == Fore.GREEN + " x " and gameboard[2][2] == Fore.GREEN + " x " and gameboard[2][3] == Fore.GREEN + " x ") or (gameboard[3][1] == Fore.GREEN + " x " and gameboard[3][2] == Fore.GREEN + " x " and gameboard[3][3] == Fore.GREEN + " x "):
        #ends loop
        playing = False

        #winner variable changed to player 1
        winner = "Player 1"

        #increases player 1's wins
        player1Wins += 1

      

      #checks if no one has won yet
      #if all of the squares have something in it, then game is a draw
      if playing:
        if gameboard[1][1] != "   " and gameboard[1][2] != "   " and gameboard[1][3] != "   " and gameboard[2][1] != "   " and gameboard[2][2] != "   " and gameboard[2][3] != "   " and gameboard[3][1] != "   " and gameboard[3][2] != "   " and gameboard[3][3] != "   ":
          #ends playing loop
          playing = False

          #chnges winner variable into a draw
          winner = "Draw"

      #checks if no one has won yet, or draw has occured
      if playing:

        #player 2's turn
        player2 = input(Fore.CYAN + Style.BRIGHT +"P2." + Style.RESET_ALL + " Enter square to play (e.g. 1,1 (column, row)):\n")

        #checks for valid input
        while player2 not in spaces or len(player2) != 3 or gameboard[int(player2[-1])][int(player2[0])] != "   ":
          player2 = input("Invalid.\n" + Fore.CYAN + Style.BRIGHT + "P2." + Style.RESET_ALL + " Enter square to play (e.g. 1,1 (column, row)):\n")

        #adds player 2's selection to the gameboard
        gameboard[int(player2[-1])][int(player2[0])] = Fore.CYAN + Style.BRIGHT + " o "



        #clears screen for updated gameboard
        print("\033[2J\033[H")

        #prints the new gameboard
        for row in gameboard:
          for element in row:
            rows+=element
          print(rows)
          rows = ""



        #Checks for player 2 win by checking all win possibilities for 3 in a row
        if (gameboard[1][1] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[1][2] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[1][3] == Fore.CYAN + Style.BRIGHT + " o ") or (gameboard[1][1] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[2][1] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[3][1] == Fore.CYAN + Style.BRIGHT + " o ") or (gameboard[1][1] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[2][2] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[3][3] == Fore.CYAN + Style.BRIGHT + " o ") or (gameboard[1][2] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[2][2] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[3][2] == Fore.CYAN + Style.BRIGHT + " o ") or (gameboard[1][3] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[2][3] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[3][3] == Fore.CYAN + Style.BRIGHT + " o ") or (gameboard[1][3] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[2][2] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[3][1] == Fore.CYAN + Style.BRIGHT + " o ") or (gameboard[2][1] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[2][2] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[2][3] == Fore.CYAN + Style.BRIGHT + " o ") or (gameboard[3][1] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[3][2] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[3][3] == Fore.CYAN + Style.BRIGHT + " o "):
          playing = False
          winner = "Player 2"
          player2Wins += 1







    #instructions for cpu game mode
    elif cpu == "cpu":

      #checks for win/ draw
      while playing:


        #player 1's input
        player1 = input("Enter square to play (e.g. 1,1 (column, row)):\n")

        #checks for valid input
        while player1 not in spaces or len(player1) != 3 or gameboard[int(player1[-1])][int(player1[0])] != "   ":
          player1 = input("Invalid.\nEnter square to play (e.g. 1,1 (column, row)):\n")

        #adds player 2's selection to gameboard
        gameboard[int(player1[-1])][int(playlist er1[0])] = Fore.GREEN + " x "
        

            
        #clears screen for new gameboard
        print("\033[2J\033[H")

        #prints updated gameboard
        for row in gameboard:
          for element in row:
            rows+=element
          print(rows)
          rows = ""



        #checks for player 1 win by checking all win possibilitues for 3 in a row
        if (gameboard[1][1] == Fore.GREEN + " x " and gameboard[1][2] == Fore.GREEN + " x " and gameboard[1][3] == Fore.GREEN + " x ") or (gameboard[1][1] == Fore.GREEN + " x " and gameboard[2][1] == Fore.GREEN + " x " and gameboard[3][1] == Fore.GREEN + " x ") or (gameboard[1][1] == Fore.GREEN + " x " and gameboard[2][2] == Fore.GREEN + " x " and gameboard[3][3] == Fore.GREEN + " x ") or (gameboard[1][2] == Fore.GREEN + " x " and gameboard[2][2] == Fore.GREEN + " x " and gameboard[3][2] == Fore.GREEN + " x ") or (gameboard[1][3] == Fore.GREEN + " x " and gameboard[2][3] == Fore.GREEN + " x " and gameboard[3][3] == Fore.GREEN + " x ") or (gameboard[1][3] == Fore.GREEN + " x " and gameboard[2][2] == Fore.GREEN + " x " and gameboard[3][1] == Fore.GREEN + " x ") or (gameboard[2][1] == Fore.GREEN + " x " and gameboard[2][2] == Fore.GREEN + " x " and gameboard[2][3] == Fore.GREEN + " x ") or (gameboard[3][1] == Fore.GREEN + " x " and gameboard[3][2] == Fore.GREEN + " x " and gameboard[3][3] == Fore.GREEN + " x "):
          #ends loops
          playing = False

          #Winer is the player
          winner = "Player"

          #wins for player against cpu increased
          player1cpuWins += 1


        #checks for draw if no one has won by checking of every square has something in it  
        elif gameboard[1][1] != "   " and gameboard[1][2] != "   " and gameboard[1][3] != "   " and gameboard[2][1] != "   " and gameboard[2][2] != "   " and gameboard[2][3] != "   " and gameboard[3][1] != "   " and gameboard[3][2] != "   " and gameboard[3][3] != "   ":
            playing = False
            winner = "Draw"



        #runs when no one has won yet / draw
        if playing:
          #reset variable for loop   
          moves = 0  

          
          #So Basically it starts off for checking every possibility for the cpu to win (24 differnet posibilities!!) if there is a possibility for cpu to win, it takes it and plays in that space.


          if (gameboard[1][1] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[1][2] == Fore.CYAN + Style.BRIGHT + " o ") and gameboard[1][3] !=Fore.GREEN + " x ":
            gameboard[1][3] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            print(10)
            
            
          elif (gameboard[1][1] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[1][3] == Fore.CYAN + Style.BRIGHT + " o ") and gameboard[1][2] !=Fore.GREEN + " x ":
            gameboard[1][2] = Fore.CYAN + Style.BRIGHT + " o " 
            moves = 1
            print(11)
            
            
          elif (gameboard[1][2] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[1][3] == Fore.CYAN + Style.BRIGHT + " o ") and gameboard[1][1] !=Fore.GREEN + " x ":
            gameboard[1][1] = Fore.CYAN + Style.BRIGHT + " o " 
            moves = 1
            
            
          elif (gameboard[2][1] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[2][2] == Fore.CYAN + Style.BRIGHT + " o ") and gameboard[2][3] !=Fore.GREEN + " x ":
            gameboard[2][3] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[2][1] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[2][3] == Fore.CYAN + Style.BRIGHT + " o ") and gameboard[2][2] !=Fore.GREEN + " x ":
            gameboard[2][2] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[2][2] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[2][3] == Fore.CYAN + Style.BRIGHT + " o ") and gameboard[2][1] !=Fore.GREEN + " x ":
            gameboard[2][1] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[3][1] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[3][2] == Fore.CYAN + Style.BRIGHT + " o ") and gameboard[3][3] !=Fore.GREEN + " x ":
            gameboard[3][3] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[3][1] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[3][3] == Fore.CYAN + Style.BRIGHT + " o ") and gameboard[3][2] !=Fore.GREEN + " x ":
            gameboard[3][2] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[3][2] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[3][3] == Fore.CYAN + Style.BRIGHT + " o ") and gameboard[3][1] !=Fore.GREEN + " x ":
            gameboard[3][1] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[1][1] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[2][1] == Fore.CYAN + Style.BRIGHT + " o ") and gameboard[3][1] !=Fore.GREEN + " x ":
            gameboard[3][1] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[1][1] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[3][1] == Fore.CYAN + Style.BRIGHT + " o ") and gameboard[2][1] !=Fore.GREEN + " x ":
            gameboard[2][1] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[2][1] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[3][1] == Fore.CYAN + Style.BRIGHT + " o ") and gameboard[1][1] !=Fore.GREEN + " x ":
            gameboard[1][1] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[1][2] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[2][2] == Fore.CYAN + Style.BRIGHT + " o ") and gameboard[3][2] !=Fore.GREEN + " x ":
            gameboard[3][2] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[1][2] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[3][2] == Fore.CYAN + Style.BRIGHT + " o ") and gameboard[2][2] !=Fore.GREEN + " x ":
            gameboard[2][2] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[2][2] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[3][2] == Fore.CYAN + Style.BRIGHT + " o ") and gameboard[1][2] !=Fore.GREEN + " x ":
            gameboard[1][2] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[1][3] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[2][3] == Fore.CYAN + Style.BRIGHT + " o ") and gameboard[3][3] !=Fore.GREEN + " x ":
            gameboard[3][3] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[1][3] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[3][3] == Fore.CYAN + Style.BRIGHT + " o ") and gameboard[2][3] !=Fore.GREEN + " x ":
            gameboard[2][3] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[2][3] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[3][3] == Fore.CYAN + Style.BRIGHT + " o ") and gameboard[1][3] !=Fore.GREEN + " x ":
            gameboard[1][3] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[1][1] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[2][2] == Fore.CYAN + Style.BRIGHT + " o ") and gameboard[3][3] !=Fore.GREEN + " x ":
            gameboard[3][3] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[1][1] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[3][3] == Fore.CYAN + Style.BRIGHT + " o ") and gameboard[2][2] !=Fore.GREEN + " x ":
            gameboard[2][2] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[2][2] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[3][3] == Fore.CYAN + Style.BRIGHT + " o ") and gameboard[1][1] !=Fore.GREEN + " x ":
            gameboard[1][1] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[1][3] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[2][2] == Fore.CYAN + Style.BRIGHT + " o ") and gameboard[3][1] !=Fore.GREEN + " x ":
            gameboard[3][1] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[1][3] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[3][1] == Fore.CYAN + Style.BRIGHT + " o ") and gameboard[2][2] !=Fore.GREEN + " x ":
            gameboard[2][2] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[2][2] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[3][1] == Fore.CYAN + Style.BRIGHT + " o ") and gameboard[1][3] !=Fore.GREEN + " x ":
            gameboard[1][3] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1




            #after checking if the cpu can win, it checks if the player is in a winning possition, if it is then the cpu will play in the location that blocks the player
            
            
          elif (gameboard[1][1] == Fore.GREEN + " x " and gameboard[1][2] == Fore.GREEN + " x ") and gameboard[1][3] == "   ":
            gameboard[1][3] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[1][1] == Fore.GREEN + " x " and gameboard[1][3] == Fore.GREEN + " x ") and gameboard[1][2] == "   ":
            gameboard[1][2] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[1][2] == Fore.GREEN + " x " and gameboard[1][3] == Fore.GREEN + " x ") and gameboard[1][1] == "   ":
            gameboard[1][1] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[2][1] == Fore.GREEN + " x " and gameboard[2][2] == Fore.GREEN + " x ") and gameboard[2][3] == "   ":
            gameboard[2][3] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[2][1] == Fore.GREEN + " x " and gameboard[2][3] == Fore.GREEN + " x ") and gameboard[2][2] == "   ":
            gameboard[2][2] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[2][2] == Fore.GREEN + " x " and gameboard[2][3] == Fore.GREEN + " x ") and gameboard[2][1] == "   ":
            gameboard[2][1] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[3][1] == Fore.GREEN + " x " and gameboard[3][2] == Fore.GREEN + " x ") and gameboard[3][3] == "   ":
            gameboard[3][3] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[3][1] == Fore.GREEN + " x " and gameboard[3][3] == Fore.GREEN + " x ") and gameboard[3][2] == "   ":
            gameboard[3][2] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[3][2] == Fore.GREEN + " x " and gameboard[3][3] == Fore.GREEN + " x ") and gameboard[3][1] == "   ":
            gameboard[3][1] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[1][1] == Fore.GREEN + " x " and gameboard[2][1] == Fore.GREEN + " x ") and gameboard[3][1] == "   ":
            gameboard[3][1] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[1][1] == Fore.GREEN + " x " and gameboard[3][1] == Fore.GREEN + " x ") and gameboard[2][1] == "   ":
            gameboard[2][1] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[2][1] == Fore.GREEN + " x " and gameboard[3][1] == Fore.GREEN + " x ") and gameboard[1][1] == "   ":
            gameboard[1][1] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[1][2] == Fore.GREEN + " x " and gameboard[2][2] == Fore.GREEN + " x ") and gameboard[3][2] == "   ":
            gameboard[3][2] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[1][2] == Fore.GREEN + " x " and gameboard[3][2] == Fore.GREEN + " x ") and gameboard[2][2] == "   ":
            gameboard[2][2] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[2][2] == Fore.GREEN + " x " and gameboard[3][2] == Fore.GREEN + " x ") and gameboard[1][2] == "   ":
            gameboard[1][2] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[1][3] == Fore.GREEN + " x " and gameboard[2][3] == Fore.GREEN + " x ") and gameboard[3][3] == "   ":
            gameboard[3][3] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[1][3] == Fore.GREEN + " x " and gameboard[3][3] == Fore.GREEN + " x ") and gameboard[2][3] == "   ":
            gameboard[2][3] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[2][3] == Fore.GREEN + " x " and gameboard[3][3] == Fore.GREEN + " x ") and gameboard[1][3] == "   ":
            gameboard[1][3] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[1][1] == Fore.GREEN + " x " and gameboard[2][2] == Fore.GREEN + " x ") and gameboard[3][3] == "   ":
            gameboard[3][3] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[1][1] == Fore.GREEN + " x " and gameboard[3][3] == Fore.GREEN + " x ") and gameboard[2][2] == "   ":
            gameboard[2][2] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[2][2] == Fore.GREEN + " x " and gameboard[3][3] == Fore.GREEN + " x ") and gameboard[1][1] == "   ":
            gameboard[1][1] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[1][3] == Fore.GREEN + " x " and gameboard[2][2] == Fore.GREEN + " x ") and gameboard[3][1] == "   ":
            gameboard[3][1] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[1][3] == Fore.GREEN + " x " and gameboard[3][1] == Fore.GREEN + " x ") and gameboard[2][2] == "   ":
            gameboard[2][2] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1
            
            
          elif (gameboard[2][2] == Fore.GREEN + " x " and gameboard[3][1] == Fore.GREEN + " x ") and gameboard[1][3] == "   ":
            gameboard[1][3] = Fore.CYAN + Style.BRIGHT + " o "
            moves = 1



            #if the player and the cpu are in no place to win, then cpu plays in a random position (e.g. happens at start of game)

          #loops until it has made a move
          while moves != 1 :

            #random nmber corresponds to square
            choice = randint(1,9)

            #if it choice is:
            #1 then it plays top left,
            #2 top middle,
            #3 top right,
            #4 middle left,
            #5 middle middle,
            #6 middle right,
            #7 bottom left,
            #8 bottom middle,
            #9 bottom right


            if choice == 1:
              #just checking that the square it is about to play to dosen't already have anything in it
              if gameboard[1][1] != Fore.GREEN + " x ":
                gameboard[1][1] = Fore.CYAN + Style.BRIGHT + " o "
                moves = 1                
                
            if choice == 2 and moves != 1:
              #just checking that the square it is about to play to dosen't already have anything in it
              if gameboard[1][2] != Fore.GREEN + " x ":
                gameboard[1][2] = Fore.CYAN + Style.BRIGHT + " o "
                moves = 1
                
            if choice == 3 and moves != 1:
              #just checking that the square it is about to play to dosen't already have anything in it
              if gameboard[1][3] != Fore.GREEN + " x ":
                gameboard[1][3] = Fore.CYAN + Style.BRIGHT + " o "
                moves = 1
                
            if choice == 4 and moves != 1:
              #just checking that the square it is about to play to dosen't already have anything in it
              if gameboard[2][1] != Fore.GREEN + " x ":
                gameboard[2][1] = Fore.CYAN + Style.BRIGHT + " o "
                moves = 1
                
            if choice == 5 and moves != 1:
              #just checking that the square it is about to play to dosen't already have anything in it
              if gameboard[2][2] != Fore.GREEN + " x ":
                gameboard[2][2] = Fore.CYAN + Style.BRIGHT + " o "
                moves = 1
                
            if choice == 6 and moves != 1:
              #just checking that the square it is about to play to dosen't already have anything in it
              if gameboard[2][3] != Fore.GREEN + " x ":
                gameboard[2][3] = Fore.CYAN + Style.BRIGHT + " o "
                moves = 1
                
            if choice == 7 and moves != 1:
              #just checking that the square it is about to play to dosen't already have anything in it
              if gameboard[3][1] != Fore.GREEN + " x ":
                gameboard[3][1] = Fore.CYAN + Style.BRIGHT + " o "
                moves = 1
                
            if choice == 8 and moves != 1:
              #just checking that the square it is about to play to dosen't already have anything in it
              if gameboard[3][2] != Fore.GREEN + " x ":
                gameboard[3][2] = Fore.CYAN + Style.BRIGHT + " o "
                moves = 1
                
            if choice == 9 and moves != 1:
              #just checking that the square it is about to play to dosen't already have anything in it
              if gameboard[3][3] != Fore.GREEN + " x ":
                gameboard[3][3] = Fore.CYAN + Style.BRIGHT + " o "
                moves = 1
          
          
              


          #clears screen for new gameboard after cpu move
          print("\033[2J\033[H")

          #prints new gameboard
          for row in gameboard:
            for element in row:
              rows+=element
            print(rows)
            rows = ""



          #checks for cpu win by checking all win possibilituies for 3 in a row
          if (gameboard[1][1] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[1][2] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[1][3] == Fore.CYAN + Style.BRIGHT + " o ") or (gameboard[1][1] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[2][1] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[3][1] == Fore.CYAN + Style.BRIGHT + " o ") or (gameboard[1][1] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[2][2] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[3][3] == Fore.CYAN + Style.BRIGHT + " o ") or (gameboard[1][2] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[2][2] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[3][2] == Fore.CYAN + Style.BRIGHT + " o ") or (gameboard[1][3] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[2][3] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[3][3] == Fore.CYAN + Style.BRIGHT + " o ") or (gameboard[1][3] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[2][2] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[3][1] == Fore.CYAN + Style.BRIGHT + " o ") or (gameboard[2][1] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[2][2] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[2][3] == Fore.CYAN + Style.BRIGHT + " o ") or (gameboard[3][1] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[3][2] == Fore.CYAN + Style.BRIGHT + " o " and gameboard[3][3] == Fore.CYAN + Style.BRIGHT + " o "):

            #ends loop
            playing = False

            #Winner is the computer
            winner = "Computer"

            #increases computer's wins
            cpuWins += 1



  #print statemnt of winner (if it was a draw print draw etc.)
  if winner == "Draw":
    print("Draw!")
  else: 
    #prints winner variable that was assigned when win was found
    print(winner + " Wins!")


  #prints log of how many wins each player has depending on what gamemode has just been played
  if cpu == "cpu":
    print("Player Wins: " + str(player1cpuWins) + "\nComputer Wins: " + str(cpuWins))
  else:
    print("Player 1 Wins: " + str(player1Wins) + "\nPlayer 2 Wins: " + str(player2Wins))




  #asks to play again (if y input, whole thing looped again (except for bit at start))
  playAgain = input("Play again (y/n):\n").lower()

  #checks for valid input
  while playAgain not in ["y", "n"]:
    playAgain = input("Invalid.\nPlay again (y/n):\n").lower()


#when the player decides they don't want to play again, screen is cleared and goodbye message printed
print("\033[2J\033[H")
print("Upvote if you had fun!\n\n\n\nBYE!")
