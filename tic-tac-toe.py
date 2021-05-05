board = [' ']*9
used_spaces = ['']
#name: print_positions
#description: prints the board, showing the numbers of the positions
#inputs: none
#returns: none
def print_positions():
  global board
  for i in range(0,len(board)):
    board[i] = str(i+1)
  print_board()
  board = [' ']*9

#name: print_board()
#description: Prints the board, showing the current state of X, O, and blanks
#inputs: none
#returns: none
def print_board():
  print()
  print(" " + board[0],"|",board[1],"|",board[2], "\n","--+---+---","\n",board[3],"|",board[4],"|",board[5],"\n","--+---+---", "\n",board[6],"|",board[7],"|",board[8],"\n")
  
#name: get_valid_user_input
#description: Only allows the user to enter a digit 1 through 9
#inputs: none
#returns: none
def get_valid_user_input():
	while True:
		where = input("\nWhere do you want to move, " + player +"? ")
		if where.isdigit():
			response = int(where)
			if response >= 1 and response < 10:
				return response-1
		print("\nYou must enter a number between 1 and 9")

#name: has_player_won
#description: tests if the player has won
#inputs: string
#returns: true or false
def has_player_won(player_turn): #player_turn is either x or o
  winners = [
    # horizontal
    [0,1,2],
    [3,4,5],
    [6,7,8],
    # vertical
    [0,3,6],
    [1,4,7],
    [2,5,8],
    # diagonal
    [0,4,8],
    [2,4,6]
  ]
    # TODO(student): Add code to test if the player has won
    # with this line. Set the variable `win` accordingly.
  for i in winners: #iterates through the list of winning trios
    #print(i)
    win = True #assume win is true at the start of each winning trio check
    for j in i: #iterates through each space in a winning trio
      #print(j)
      if board[j] == player_turn and win: #checks to see if all the other spaces in the winning trio are filled by the same player
        win = True #win will only be true if all other spaces in the winning trio are filled by the player who just went
      else:
        win = False #if the player who has just gone is missing any spaces in a winning trio, there is no winner yet
      #win = board[j] == player_turn and win 
      #print(win)
    if win: #if win is still true at the end of a winning trio check, it means that the player whose turn it just was has won.
      return True #this ends function (and the game)
  if not win: #if win is still not true after all winnin trios have been checked, it means no one has won yet, and the game continues
    return False

#name: is_a_tie
#description: returns True if there is a tie, else return False
#inputs: none
#returns: true or false
def is_a_tie():
  if total_turns == 10 and not has_player_won(player):
    return True

#name: play_again
#description: allows the user to restart or quit
#inputs: none
#returns: true or false
def play_again():
  response = False
  while not response:
    restart = input("\nDo you want to play again? (y for yes and n for no)")
    if restart == "y":
      response = True
      return False
    elif restart == "n":
      response = True
      return True
    else:
      response = False

# Main game loop
import random
turn = random.randint(1,2)
total_turns = 1
game_over = False
print_positions()
while not game_over:
  if turn % 2 == 0:
    player = "O"
  else:
    player = "X"
  # print the board
  print_board()
  valid_move = False
  while not valid_move:
    # Get valid input
    user1_choice = get_valid_user_input()
    if user1_choice not in used_spaces:
      used_spaces.append(user1_choice)
    # Is the move valid (Is position not occupied)?
      # if yes, mark the player as having that position on the board
      board[user1_choice] = player
      valid_move = True
      turn +=1
      total_turns +=1
    else:
      print("\nThat space is taken. Try Again.")
  # Is there a winner?
  if has_player_won(player):
      print_board()
      # Print which player won
      print("\n" + player + " wins")
      if not play_again():
        # if yes, clear the board
        total_turns = 1
        turn = random.randint(1,2)
        print_positions()
        used_spaces = ['']
      else:
        # if no, game_over = True
        game_over = True
  # Was there a tie?
  if is_a_tie():
      print_board()
      # Print that there was a tie
      print("\nIt's a tie!")
      #Ask if you want to play again
      if not play_again():
        # if yes, clear the board
        total_turns = 1
        turn = random.randint(1,2)
        print_positions()
        used_spaces = ['']
      else:
        # if no, game_over = True
        game_over = True
print("\nAwww, why'd you stop?")