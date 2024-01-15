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
import sys

pygame.init()

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255 ,0 ,0)
YELLOW = (255, 255, 0)

ROW_COUNT = 10
COL_COUNT = 10

SQUARE_SIZE = 75
width = COL_COUNT * SQUARE_SIZE
height = ROW_COUNT * SQUARE_SIZE
size = (width, height)

CIRCLE_RAD = int(SQUARE_SIZE / 2 - 5)

font = pygame.font.SysFont(None, 75)



def create_board():
    '''creates the game board'''
    board = np.zeros((ROW_COUNT, COL_COUNT))
    return board

def drop_peice(board, row, col, peice):
    """sets the row and column in which the peice has been dropped"""
    board[row][col] = peice

def is_valid_location(board, col):
    """returns False is there is no peice at that row, column location"""
    is_there_a_peice = board[ROW_COUNT - 1][col]
    if is_there_a_peice == 0:
        return True
    return False

def next_empty_row(board, col):
    '''finds the nect empty row and returns its index'''
    for row in range(ROW_COUNT):
        if board[row][col] == 0:
            return row

def print_board(board):
    """function to print the game board"""
    print(np.flip(board, 0))

def winning_move_connect_3(board, peice):
    '''checks and return True if the winning move for connect 3 i played'''
    for col in range(COL_COUNT - 3):
        for row in range(ROW_COUNT):
            if board[row][col] == peice and board[row][col + 1] == peice and board[row][col + 2] == peice and board[row][col + 3]:
                return True # winning move by 4 in a row horizontally
    
    for col in range(COL_COUNT):
        for row in range(ROW_COUNT - 3):
            if board[row][col] == peice and board[row + 1][col] == peice and board[row + 2][col] == peice and board[row + 3][col]:
                return True # winning move by 4 in a row vertically
            
    for col in range(COL_COUNT - 3):
        for row in range(3, ROW_COUNT):
            if board[row][col] == peice and board[row - 1][col + 1] == peice and board[row - 2][col + 2] == peice and board[row - 3][col + 3]:
                return True # winning move by 4 in a row diagonal slope downwards
            
    for col in range(COL_COUNT - 3):
        for row in range(ROW_COUNT - 3):
            if board[row][col] == peice and board[row + 1][col + 1] == peice and board[row + 2][col + 2] == peice and board[row + 3][col + 3]:
                return True # winning move by 4 in a row diagonal slope upwards


def winning_move_for_connect_x(board, peice, x):
    """ generalised algo for any game of connect_x """
    for col in range(COL_COUNT - x - 1):
        for row in range(ROW_COUNT):
            in_a_row = 0 
            z = 0 
            while z < (x):
                if board[row][col + z] == peice:
                    in_a_row += 1
                else:
                    in_a_row = 0
                z += 1
            if in_a_row == x:
                return True # winning move by 4 in a row horizontally
    for col in range(COL_COUNT):
        for row in range(ROW_COUNT - x - 1):
            in_a_row = 0
            z = 0 
            while z < (x):
                if board[row + z][col] == peice:
                    in_a_row += 1
                else:
                    in_a_row = 0
                z += 1
            if in_a_row == x:
                return True # winning move by 4 in a row veritcally
            
    for col in range(COL_COUNT - x - 1):
        for row in range(ROW_COUNT):
            z = 0 
            in_a_row = 0
            while z < (x):
                if board[row - z][col + z] == peice:
                    in_a_row += 1
                else:
                    in_a_row = 0 
                z += 1
            if in_a_row == x:
                return True # winning move by 4 in a row diagonally
            
    for col in range(COL_COUNT - x - 1):
        for row in range(ROW_COUNT - x - 1):
            z = 0 
            in_a_row = 0
            while z < (x):
                if board[row + z][col + z] == peice:
                    in_a_row += 1
                else:
                    in_a_row = 0 
                z += 1
            if in_a_row == x:
                return True # winning move by 4 in a row diaganlly
    



def draw_board(board, SCREEN):
	for col in range(COL_COUNT):
		for row in range(ROW_COUNT):
			pygame.draw.rect(SCREEN, BLUE, (col * SQUARE_SIZE, row * SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
			pygame.draw.circle(SCREEN, BLACK, (int(col * SQUARE_SIZE+SQUARE_SIZE / 2), int(row * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)), CIRCLE_RAD)
	
	for col in range(COL_COUNT):
		for row in range(ROW_COUNT):		
			if board[row][col] == 1:
				pygame.draw.circle(SCREEN, RED, (int(col * SQUARE_SIZE+SQUARE_SIZE / 2), height - int(row * SQUARE_SIZE+SQUARE_SIZE / 2)), CIRCLE_RAD)
			elif board[row][col] == 2: 
				pygame.draw.circle(SCREEN, YELLOW, (int(col * SQUARE_SIZE+SQUARE_SIZE / 2), height - int(row * SQUARE_SIZE+SQUARE_SIZE / 2)), CIRCLE_RAD)
	pygame.display.update()



def main():
    """the mains game loop"""
    connect_x = 4
    SCREEN = pygame.display.set_mode(size)
    board = create_board()
    #print_board(board)
    draw_board(board, SCREEN)
    pygame.display.update()
    full_game_over = False
    turn  = 0
    while full_game_over is False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(SCREEN, BLACK, (0, 0, width, SQUARE_SIZE))
                position_x = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(SCREEN, RED, (position_x, int(SQUARE_SIZE / 2)), CIRCLE_RAD)
                else:
                    pygame.draw.circle(SCREEN, YELLOW, (position_x, int(SQUARE_SIZE / 2)), CIRCLE_RAD)
            #print_board(board)
            draw_board(board, SCREEN)
            pygame.display.update()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(SCREEN, BLACK, (0, 0, width, SQUARE_SIZE))
                if turn == 0:
                    position_x = event.pos[0]
                    col = int(math.floor(position_x / SQUARE_SIZE))
                    
                    if is_valid_location(board, col) is True:
                        row = next_empty_row(board, col)
                        drop_peice(board, row, col, 1)
                        
                        if winning_move_for_connect_x(board, 1, connect_x) is True:
                            label = font.render("Player 1 wins!!", 1, RED)
                            print('player 1 wins')
                            SCREEN.blit(label, (40,10))
                            full_game_over = True
                else:
                    position_x = event.pos[0]
                    col = int(math.floor(position_x / SQUARE_SIZE))
                    
                    if is_valid_location(board, col) is True:
                        row = next_empty_row(board, col)
                        drop_peice(board, row, col, 2)
                        
                        if winning_move_for_connect_x(board , 2, connect_x):
                            label = font.render("Player 1 wins!!", 1, RED)
                            print('player 2 wins')
                            SCREEN.blit(label, (40,10))
                            full_game_over = True
                            
                #print_board(board)
                draw_board(board, SCREEN)
                
                turn = (turn + 1) % 2 
                if full_game_over is True:
                    pygame.time.wait(8000)
                
                            
                    
                        

                
main()

                
                    
                 


