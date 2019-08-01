#!/usr/bin/env python3
# -*- coding: utf-8 -*

"""
An AI player for Othello. This is the template file that you need to  
complete and submit for the competition. 

@author: Hao Teng
"""

import random
import sys
import time
import math

# You can use the functions in othello_shared to write your AI 
from othello_shared import find_lines, get_possible_moves, get_score, play_move, play_move2

def compute_utility(board, color):
    return 0


############ MINIMAX ###############################

def minimax_min_node(board, color):
    newBoards = dict()
    newBoardsScore = dict()
    currentMin = math.inf
    current_board_with_move = None
    
    if (get_possible_moves(board,color)):
        allowedMoves = get_possible_moves(board,color)
    
        for i in range(len(allowedMoves)):
            newBoards[i] = board[:]
            #Create a new board with the intended move
            newBoards[i] = [play_move(newBoards[i],color,allowedMoves[i][0],allowedMoves[i][1]),(allowedMoves[i][0],allowedMoves[i][1])]
            newBoardsScore[i] = get_score(newBoards[i][0])
            #Assume Ai is player 1
            if newBoardsScore [i][0] < currentMin:
                currentMin = newBoardsScore[i][0]
                current_board_with_move = newBoards[i]

        return [currentMin,current_board_with_move]
    else:
        return None



def minimax_max_node(board, color):
    newBoards = dict()
    newBoardsScore = dict()
    currentMax = -(math.inf)
    current_board_with_move = None
    
    if (get_possible_moves(board,color)):
        allowedMoves = get_possible_moves(board,color)
    
        for i in range(len(allowedMoves)):
            newBoards[i] = board[:]
            #Create a new board with the intended move
            newBoards[i] = [play_move(newBoards[i],color,allowedMoves[i][0],allowedMoves[i][1]),(allowedMoves[i][0],allowedMoves[i][1])]
            newBoardsScore[i] = get_score(newBoards[i][0])
            #Assume Ai is player 1
            if newBoardsScore [i][0] > currentMax:
                currentMax = newBoardsScore[i][0]
                current_board_with_move = newBoards[i]

        return [currentMax,current_board_with_move]
    else:
        return None

    
def select_move_minimax(board, color):
    """
    Given a board and a player color, decide on a move. 
    The return value is a tuple of integers (i,j), where
    i is the column and j is the row on the board.  
    """

    #Color 1 is black and  color 2 is White

    #try to max the color's score
    
#    if (color == 1):
#        opp = 2
#    else:
#        opp = 1
        
    maxVal = True

    returnedValue = []
    
    returnedValue.append(None)
    returnedValue.append(board)

    if (len(returnedValue[1]) == 2):
        while(get_possible_moves(returnedValue[1][0],color)):
            if (maxVal):
                returnedValue = minimax_max_node(returnedValue[1][0],color)
                color = 1
                maxVal = False
            else:
                returnedValue = minimax_min_node(returnedValue[1][0],color)
                color = 2
                maxVal = True
    else:
        while(get_possible_moves(returnedValue[1],color)):
            if (maxVal):
                returnedValue = minimax_max_node(returnedValue[1][0],color)
                color = 1
                maxVal = False
            else:
                returnedValue = minimax_min_node(returnedValue[1][0],color)
                color = 2
                maxVal = True  
    
    return returnedValue

    #return best_val, best_move
    
############ ALPHA-BETA PRUNING #####################

#alphabeta_min_node(board, color, alpha, beta, level, limit)
def alphabeta_min_node(board, color, alpha, beta): 
    return None


#alphabeta_max_node(board, color, alpha, beta, level, limit)
def alphabeta_max_node(board, color, alpha, beta):
    return None


def select_move_alphabeta(board, color): 

    return 0,0 


####################################################
def run_ai():
    """
    This function establishes communication with the game manager. 
    It first introduces itself and receives its color. 
    Then it repeatedly receives the current score and current board state
    until the game is over. 
    """
    print("Minimax AI") # First line is the name of this AI  
    color = int(input()) # Then we read the color: 1 for dark (goes first), 
                         # 2 for light. 

    #print("2")

    while True: # This is the main loop 
        # Read in the current game status, for example:
        # "SCORE 2 2" or "FINAL 33 31" if the game is over.
        # The first number is the score for player 1 (dark), the second for player 2 (light)
        next_input = input() 
        status, dark_score_s, light_score_s = next_input.strip().split()
        dark_score = int(dark_score_s)
        light_score = int(light_score_s)

        if status == "FINAL": # Game is over. 
            print 
        else: 
            board = eval(input()) # Read in the input and turn it into a Python
                                  # object. The format is a list of rows. The 
                                  # squares in each row are represented by 
                                  # 0 : empty square
                                  # 1 : dark disk (player 1)
                                  # 2 : light disk (player 2)
                    
            # Select the move and send it to the manager 
            movei, movej = select_move_minimax(board, color)
            #movei, movej = select_move_alphabeta(board, color)
            print("{} {}".format(movei, movej)) 


if __name__ == "__main__":
    run_ai()
