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

# You can use the functions in othello_shared to write your AI 
from othello_shared import find_lines, get_possible_moves, get_score, play_move

def compute_utility(board, color):
    return 0


############ MINIMAX ###############################

# def minimax_min_node(board, color):
#     return None


# def minimax_max_node(board, color):
#     return None 

def minimax(board, depth, isMaximize, color):
    if depth == 0 or not get_possible_moves(board, color):
    #if not get_possible_moves(board, color):
        score1, score2 = get_score(board)
        if (color == 1):
            return score1,None
        elif(color == 2):
            return score2,None
    
    newBoards = list()
    moves = dict()

    possibleMoves = get_possible_moves(board,color)
    for i in range(len(possibleMoves)):
        newBoards.append(play_move(board,color,possibleMoves[i][0],possibleMoves[i][1]))
        moves[play_move(board,color,possibleMoves[i][0],possibleMoves[i][1])] = possibleMoves[i]

    if isMaximize:
        maxVal = -(float("inf"))
        bestMove = moves[newBoards[0]]
        for i in range(len(newBoards)):
            val,move = minimax(newBoards[i], depth-1,False, color)
            maxVal = max(maxVal, val)
            #Add the move for return when the new value is better
            if (max(maxVal,val) == val):
                bestMove = moves[newBoards[i]]
                #currentMove = move
            if (color ==1):
                color = 2
            else:
                color = 1
        return maxVal,bestMove
    else:
        minVal = float('inf')
        bestMove = moves[newBoards[0]]
        for i in range(len(newBoards)):
            val,move = minimax(newBoards[i],depth-1,True, color)
            minVal = min(minVal,val)
            #Add the move for return when the new value is better
            if (min(minVal,val) == val):
                bestMove = moves[newBoards[i]]
                #currentMove = move
            if (color ==1):
                color = 2
            else:
                color = 1
        return minVal,bestMove
        


    
def select_move_minimax(board, color):
    """
    Given a board and a player color, decide on a move. 
    The return value is a tuple of integers (i,j), where
    i is the column and j is the row on the board.  
    """
    val,move = minimax(board,float('inf'),True,color)

    #print(val,0)
    return move
#    return 0,0
    
############ ALPHA-BETA PRUNING #####################

#alphabeta_min_node(board, color, alpha, beta, level, limit)
def alphabeta_min_node(board, color, alpha, beta): 
    return None


#alphabeta_max_node(board, color, alpha, beta, level, limit)
def alphabeta_max_node(board, color, alpha, beta):
    return None

def alphabeta(board, depth, isMaximize, color, alpha,beta):

    # if isMaximize:
    #     color = 1
    # else:
    #     color = 2

    if depth == 0 or not get_possible_moves(board, color):
    #if not get_possible_moves(board, color):
        score1, score2 = get_score(board)
        if (color == 1):
            return score1,None
        elif(color == 2):
            return score2,None
        #return
    
    newBoards = list()
    moves = dict()

    possibleMoves = get_possible_moves(board,color)
    for i in range(len(possibleMoves)):
        newBoards.append(play_move(board,color,possibleMoves[i][0],possibleMoves[i][1]))
        moves[play_move(board,color,possibleMoves[i][0],possibleMoves[i][1])] = possibleMoves[i]

    if isMaximize:
        maxVal = -(float("inf"))
        for i in range(len(newBoards)):
            val,move = alphabeta(newBoards[i], depth-1,False, color, alpha,beta)
            if (color ==1):
                color = 2
            else:
                color = 1
            if (max(maxVal,val) == val):
                bestMove = moves[newBoards[i]]

            maxVal = max(maxVal, val)  
            alpha = max(alpha, maxVal)  
  
            # Alpha Beta Pruning  
            if beta <= alpha:  
                break 
        return maxVal,bestMove
    else:
        minVal = float('inf')
        for i in range(len(newBoards)):
            val,move = alphabeta(newBoards[i],depth-1,True, color, alpha, beta)
            if (color ==1):
                color = 2
            else:
                color = 1
            if (min(minVal,val) == val):
                bestMove = moves[newBoards[i]]

            minVal = min(minVal, val)  
            beta = min(beta, minVal)  
  
            # Alpha Beta Pruning  
            if beta <= alpha:  
                break 
        return minVal,bestMove

def select_move_alphabeta(board, color): 
    val,move = alphabeta(board,6,True, color, -10000, 10000)
    return move
    #return 0,0


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
            #movei, movej = select_move_minimax(board, color)
            movei, movej = select_move_alphabeta(board,color)
            print("{} {}".format(movei, movej)) 


if __name__ == "__main__":
    run_ai()
