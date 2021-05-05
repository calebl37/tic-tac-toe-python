board=[]
import math
import random


def print_board(sidelength):
  row = ''
  for i in range(0,(sidelength*sidelength)):
    row += "| " + board[i] + " "
    if (i+1) % sidelength == 0:
      print("+---"*sidelength + "+")
      print(row + "|")
      row = ''
  print("+---"*sidelength + "+")





def check_win(player,sidelength):
  for j in range(0,sidelength): #0,1,2...sidelength - 1
    win_vert = True 
    win_horiz = True
    win_diag1 = True
    win_diag2 = True
    for i in range(0,len(board)):
      if i % sidelength == j: #vertical check column j
        if board[i] == player and win_vert:
          win_vert = True
        else:
          win_vert = False
      if i >= sidelength*j and i < sidelength*(j+1): #horizontal check row j
        if board[i] == player and win_horiz:
          win_horiz = True
        else:
          win_horiz = False
      if i % (sidelength+1) == 0: #diagonal 1 check
        #print(i)
        if board[i] == player and win_diag1:
          win_diag1= True
        else:
          win_diag1 = False
      if i % (sidelength - 1) == 0 and i > 0 and i < (len(board)-sidelength+1): #diagonal 2 check
        #print(i)
        if board[i] == player and win_diag2:
          win_diag2 = True
        else:
          win_diag2 = False
    return (win_vert or win_horiz or win_diag1 or win_diag2)
      

def initialize_sim():
  global board
  size = int(input("What is the side length of the tic tac toe board?"))
  board = [""]*size*size
  half = (size*size)/2

  num_x = 0
  num_o = 0
  for i in range(0,len(board)):
    player = random.randint(1,2)
    if player == 1:
      if num_x < math.ceil(half):
        board[i] = "x"
        num_x +=1
      else:
        board[i] = "o"
        num_o +=1
    else: 
      if num_o < math.floor(half):
        board[i] = "o"
        num_o +=1
      else:
        board[i] = "x"
        num_x +=1
  
  

  print_board(size)

  print("x winner: " + str(check_win("x",size)))
  print("o winner: " + str(check_win("o",size)))
  again = input("Sim again? (y/n)")
  if again == "y":
    initialize_sim()


initialize_sim()