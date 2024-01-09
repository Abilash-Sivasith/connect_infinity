"""
Connect Infinity

Rules:
    - First connect 4 is played as normally
    - After a winner of connect 4 is decided, connect 5 will begin on the same board (previous counters will be left on the board and are still active)
    - When playing connect 5 each player will get 2 counters per turn
    - After the games finished then connect 6 will be played (same board and previous counters from connect 4 and 5 are active)
    - The player who has won the most rounds of connect game win. 
"""

import numpy as np
import pygame
import math

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255 ,0 ,0)
YELLOW = (255, 255, 0)

ROW_COUNT = 10
COL_COUNT = 10

CURRENT_CONNECT_GAME = 3

def create_board():
    '''creates the game board'''
    board = np.zeros((ROW_COUNT, COL_COUNT))
    return board

def drop_peice(board, row, col, peice):
    """sets the row and column in which the peice has been dropped"""
    board[row][col] = peice

def is_valid_location(board, col, row):
    """returns False is there is no peice at that row, column location"""
    is_there_a_peice = board[row][col]
    if is_there_a_peice == 0:
        return False
    return True

def next_empty_row(board, col):
    '''finds the nect empty row and returns its index'''
    for row in range(ROW_COUNT):
        if board[row][col] == 0:
            return row

def print_board(board):
    """function to print the game board"""
    print(np.flip(print_board, 0))

def winning_move_connect_3(board, peice):
    '''checks and return True if the winning move for connect 3 i played'''
    for col in range(COL_COUNT - 3):
        for row in range(ROW_COUNT):
            if board[row][col] == peice and board[row][col + 1] == peice and board[row][col + 2] == peice:
                return True # winning move by 3 in a row horizontally
    
    for col in range(COL_COUNT):
        for row in range(ROW_COUNT - 3):
            if board[row][col] == peice and board[row + 1][col] == peice and board[row + 2][col] == peice:
                return True # winning move by 3 in a row vertically
            
    for col in range(COL_COUNT - 3):
        for row in range(3, ROW_COUNT):
            if board[row][col] == peice and board[row - 1][col + 1] == peice and board[row - 3][col + 3] == peice:
                return True # winning move by 3 in a row diagonal slope downwards
    for col in range(COL_COUNT - 3):
        for row in range(ROW_COUNT - 3):
            if board[row][col] == peice and board[row + 1][col + 1] == peice and board[row + 2][col + 2] == peice:
                return True # winning move by 3 in a row diagonal slope upwards



def main():
    """the mains game loop"""
    game_over = False
    while game_over is False:
        pass


