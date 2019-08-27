# Tic Tac Toe
# 27 Aug 2019
# First Project on Python

# using this library to clear up the terminal window
import os

# Make a global list of postions
L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# to color the Xs and Os
colors = {'reset':'\033[0m', 'blue':'\033[34m', 'red':'\033[31m'}

def main():  
  # Loop to take input from user until correct value given
  while True:

    # clear terminal screen
    os.system('cls||clear')

    # Calls function to display grid
    display_grid()

    # Player 1 ==> X
    while True:
      # take input from player 1
      # try/except to catch any error thrown by prgram when not an INT given by user
      try:
        player_x = int(input("PLAYER ONE: Please enter your value between 1 to 9: "))
      except ValueError:
        print("Sorry, the value you entered is not integer.")
        continue

      # check if value entered is correct and not taken already
      if player_x >= 1 and player_x <= 9 and type(L[player_x-1]) is int:
        L[player_x-1] = f"{colors['blue']}X{colors['reset']}"
        display_grid()
        print("")
        break
      
      # if value already taken, reprompt
      else:
        print("Incorrect value or Position already used. Please enter correct value")
        continue
    
    # call check function to check if win/lose or tie
    result = check()
    
    # clear terminal screen
    os.system('cls||clear')

    # Calls function to display grid
    display_grid()

    # end game if player 1 won
    if result is True:
      print("Player One Won the game! :D ")
      print("")
      break

    # call function to check if game is tied
    tie = check_tie()

    print("")
    if tie == 0:
      print("Game has been tied")
      print("")
      break

    # Player 2 ==> O
    while True:
      # take input from player 2
      # try/except to catch any error thrown by prgram when not an INT given by user
      try:
        player_o = int(input("PLAYER TWO: Please enter your value between 1 to 9: "))
      except ValueError:
        print("Sorry, the value you entered is not integer.")
        continue

      # check if value entered is correct and not taken already
      if player_o >= 1 and player_o <= 9 and type(L[player_o-1]) is int:
        L[player_o-1] = f"{colors['red']}O{colors['reset']}"
        display_grid()
        print("")
        break

      # if value incorrect or already taken, reprompt
      else:
        print("Invalid value or position already used. Please enter correct value")
        continue

    # call check function to check if win/lose or tie
    result = check()

    # clear terminal screen
    os.system('cls||clear')

    # Calls function to display grid
    display_grid()

    # end game if player 2 won
    if result is True:
      print("Player Two Won the game! :D")
      print("")
      break

# main ends  


# FUNCTIONS #

# Display Grid
def display_grid():
  
  print("********** Welcome to TIC TAC TOE **********")
  print("")
  print("")
  print(f" {L[0]}|{L[1]}|{L[2]}")
  print("-- - --")
  print(f" {L[3]}|{L[4]}|{L[5]} ")
  print("-- - --")
  print(f" {L[6]}|{L[7]}|{L[8]} ")
  print("")


def check():
  if L[0] == L[1] == L[2] or L[3] == L[4] == L[5] or L[6] == L[7] == L[8] or L[0] == L[3] == L[6] or L[1] == L[4] == L[7] or L[2] == L[5] == L[8] or L[0] == L[4] == L[8] or L[2] == L[4] == L[6]:
    return True


def check_tie():
  count = 0
  for x in range(len(L)):
    if type(L[x]) is int:
      count += 1
    
  return count 


if __name__ == "__main__":
    main()
