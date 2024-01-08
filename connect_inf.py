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



def main():
    """the mains game loop"""
    game_over = False
    while game_over is False:
        pass


