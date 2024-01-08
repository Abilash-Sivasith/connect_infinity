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

def create_board():
    '''creates the game board'''
    board = np.zeros((ROW_COUNT, COL_COUNT))
    return board

def drop_peice(board, row, col, peice):
    """sets the row and column in which the peice has been dropped"""
    board[row][col] = peice

