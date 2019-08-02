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
from othello_shared import find_lines, get_possible_moves, get_score, play_move

def compute_utility(board, color):
    return 0


############ MINIMAX ###############################

# def minimax_min_node(board, color):
#     return None


# def minimax_max_node(board, color):
#     return None 

def minimax(board, depth, color):
    if color == 1:
        isMaximize = True
    else:
        isMaximize = False

    newBoards = list()

    '''
    Base case
    '''

    if depth == 0 or not get_possible_moves(board, color):
    #if not get_possible_moves(board, color):
        score1, score2 = get_score(board)
        if (color == 1):
            return score1-score2,None
        elif(color == 2):
            return score1-score2,None

    
    moves = dict()

    ''' For every possible moves...create a new board with the individual move attached to the same list '''

    possibleMoves = get_possible_moves(board,color)

    for i in range(len(possibleMoves)):
        newBoards.append(play_move(board,color,possibleMoves[i][0],possibleMoves[i][1]))
        moves[play_move(board,color,possibleMoves[i][0],possibleMoves[i][1])] = possibleMoves[i]

    '''
    Change the color so the position changes for the next round.
    '''

    if isMaximize:
        '''
        If it is a max player...get the max score and the moves associated with it
        ''' 
        maxVal = -(math.inf)
        best_board = None

        for i in range(len(newBoards)):

            #3,None
            val,move = minimax(newBoards[i], depth-1,2)

            maxVal = max(maxVal, val) 
            if (max(maxVal,val) == val):
                best_board = newBoards[i] 
        
        bestMove = moves[best_board]
  
        return maxVal,bestMove
    else:
        '''
        If it is a min player...get the min score and the moves associated with it
        '''
        minVal = math.inf
        best_board = None

        for i in range(len(newBoards)):
            val,move = minimax(newBoards[i],depth-1,1)
            if (min(minVal,val) == val):
                best_board = newBoards[i]

            minVal = min(minVal, val) 

        bestMove = moves[best_board]

        return minVal,bestMove
        


    
def select_move_minimax(board, color):
    """
    Given a board and a player color, decide on a move. 
    The return value is a tuple of integers (i,j), where
    i is the column and j is the row on the board.  
    """
    val,move = minimax(board,math.inf,color)

    return move
    
############ ALPHA-BETA PRUNING #####################

#alphabeta_min_node(board, color, alpha, beta, level, limit)
# def alphabeta_min_node(board, color, alpha, beta): 
#     return None


#alphabeta_max_node(board, color, alpha, beta, level, limit)
# def alphabeta_max_node(board, color, alpha, beta):
#     return None

def alphabeta_run (board, depth, color, alpha, beta, maxTime):
    timerem = time.time() + maxTime
    def alphabeta(board, depth, color, alpha,beta):

        if color == 1:
            isMaximize = True
        else:
            isMaximize = False    


        '''
        Get as many pieces as possible
        '''

    #    if depth == 0 or not get_possible_moves(board, color):
    #        score1, score2 = get_score(board)
    #        return score1-score2,None

        '''
        Get as many moves as possible
        '''

        # positional_strategy = [[35,-6,8,6,6,8,-6,35],
        #                     [-6,-8,-4,-3,-3,-4,-8,-6],
        #                     [8,-3,4,4,4,4,-3,8],
        #                     [6,-2,4,3,3,4,-2,6],
        #                     [6,-2,4,3,3,4,-2,6],
        #                     [8,-3,4,4,4,4,-3,8],
        #                     [-6,-8,-4,-3,-3,-4,-8,-6],
        #                     [35,-6,8,6,6,8,-6,35]]

        positional_strategy = [[100,-20,12,6,6,12,-20,100],
                               [-20,-10,12,-3,-3,12,-10,-20],
                               [12,3,12,12,12,12,3,12],
                               [6,-3,12,3,3,12,-3,6],
                               [6,-3,12,3,3,12,-3,6],
                               [12,12,12,12,12,12,12,12],
                               [-20,-10,12,-3,-3,12,-10,-20],
                               [100,-20,12,6,6,12,-20,100]]

        '''
        Get as many points as possible with positional strategy
        '''
        
        if (time.time() >= timerem or not get_possible_moves(board,color)):
            score = 0
            for i in range(len(board)):
                for j in range(len(board)):
                    if (board[i][j] == 1):
                        score += positional_strategy[i][j]
                    elif (board[i][j] == 2):
                        score -= positional_strategy[i][j]

            p1_score, p2_score = get_score(board)
            if (color == 1):
                score += p1_score - p2_score
            elif (color == 2):
                score += p1_score - p2_score

            if (get_possible_moves(board,color)):
                if (len(get_possible_moves(board,color)) > 2):
                    score += 4
                elif (len(get_possible_moves(board,color)) > 1):
                    score += 2

            return score,None
        
        newBoards = list()
        moves = dict()

        ''' For every possible moves...create a new board with the individual move attached to the same list '''

        possibleMoves = get_possible_moves(board,color)

        for i in range(len(possibleMoves)):
            newBoards.append(play_move(board,color,possibleMoves[i][0],possibleMoves[i][1]))
            moves[play_move(board,color,possibleMoves[i][0],possibleMoves[i][1])] = possibleMoves[i]

        '''
        Change the color so the position changes for the next round.
        '''

        if isMaximize:
            '''
            If it is a max player...get the max score and the moves associated with it
            ''' 
            maxVal = -(math.inf)
            best_board = newBoards[0]

            for i in range(len(newBoards)):

                #Break after some time
                # if (time.time() > timeout):
                #     break

                val,move = alphabeta(newBoards[i], depth+1,2,alpha,beta)

                maxVal = max(maxVal, val) 
                if (max(maxVal,val) == val):
                    best_board = newBoards[i]

                alpha = max(alpha, maxVal)  
    
                # Alpha Beta Pruning  
                if beta <= alpha:
                    break
            
            bestMove = moves[best_board]
            return maxVal,bestMove

        else:
            '''
            If it is a min player...get the min score and the moves associated with it
            '''
            minVal = math.inf
            best_board = newBoards[0]

            for i in range(len(newBoards)):

                #Break after some time
                # if (time.time() > timeout):
                #     break

                val,move = alphabeta(newBoards[i],depth+1,1, alpha,beta)
                if (min(minVal,val) == val):
                    best_board = newBoards[i]

                minVal = min(minVal, val) 
                beta = min(beta, minVal)  

                # Alpha Beta Pruning  
                if beta <= alpha:  
                    break

            bestMove = moves[best_board]

            return minVal,bestMove

    val, move = alphabeta(board,depth,color,alpha,beta)
    return move

def select_move_alphabeta(board, color): 
    val,move = alphabeta_run(board,0, color, -math.inf, math.inf, 9)
    return move
    #return val,0


####################################################
def run_ai():
    """
    This function establishes communication with the game manager. 
    It first introduces itself and receives its color. 
    Then it repeatedly receives the current score and current board state
    until the game is over. 
    """
    print("Hao AI v2.1") # First line is the name of this AI  
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
