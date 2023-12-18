#!/usr/bin/python

import sys
import json
import socket

import random

def recurssive_find(board, row, col, row_increment, col_increment, pieces_passed, opponent, board_size, player):

  # If out of bounds, no possible move
  # If player's piece is on other side of opponents piece, no possible move
  if row < 0 or row > board_size or col < 0 or col > board_size or board[row][col] == player:
    return False, False, False

  # Possile move found! Return location
  if board[row][col] == 0 :
    return pieces_passed, row, col

  # No move found, keep looking
  search_row = row + row_increment
  search_col = col + col_increment
  pieces_passed += 1
  return recurssive_find(board, search_row, search_col, row_increment, col_increment, pieces_passed, opponent, board_size, player)
    

def get_move(player, board):

  opponent = 3 - player 
  board_size = len(board)-1
  valid_moves = []

  for row in range(len(board)):
    for col in range(len(board[row])):
      #Find piece of same player and begin looking for valid moves
      if board[row][col] == player:
        for row_increment in [-1,0,1]:
          for col_increment in [-1,0,1]:
            #Make sure location is in bounds
            if 0 <= row+row_increment <= board_size and 0 <= col + col_increment <= board_size:
              if board[row+row_increment][col+col_increment] == opponent:
                #Opponents piece is next to players piece, look for open moves
                pieces_passed, move_row, move_col = recurssive_find(board, row + row_increment + row_increment, col + col_increment + col_increment, row_increment, col_increment, 1, opponent, board_size, player)
                if pieces_passed: 
                  for loc in valid_moves:
                    # Check to see if location already exists in valid_moves and add pieces to that location
                    if move_row in loc[1:3] and move_col in loc[1:3]:
                      loc[0] += pieces_passed
                  else:
                    valid_moves.append([pieces_passed, move_row, move_col])

  max = [0,0,0]
  move = [0,0]
  for loc in valid_moves:
    # Find the most pieces that can be taken in one move
    if max[0] < loc[0]: max = loc
    for corner in [[0,0], [0,7], [7,0], [7,7]]:
      # Place in corner if possible
      if corner == loc[1:3]:
        move = corner
        return move

  #Otherwise take most pieces
  return max[1:3]


def prepare_response(move):
  response = '{}\n'.format(move).encode()
  print('sending {!r}'.format(response))
  return response

if __name__ == "__main__":
  port = int(sys.argv[1]) if (len(sys.argv) > 1 and sys.argv[1]) else 1337
  host = sys.argv[2] if (len(sys.argv) > 2 and sys.argv[2]) else socket.gethostname()

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    sock.connect((host, port))
    while True:
      data = sock.recv(1024)
      if not data:
        print('connection to server closed')
        break
      json_data = json.loads(str(data.decode('UTF-8')))
      board = json_data['board']
      maxTurnTime = json_data['maxTurnTime']
      player = json_data['player']
      print(player, maxTurnTime, board)

      move = get_move(player, board)
      response = prepare_response(move)
      sock.sendall(response)
  finally:
    sock.close()
