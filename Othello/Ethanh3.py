
"""
An AI player for Othello. This is the template file that you need to  
complete and submit for the competition. 

@author: YOUR NAME
"""

import random
import sys
import time

# You can use the functions in othello_shared to write your AI 
from othello_shared import find_lines, get_possible_moves, get_score, play_move


############ ALPHA-BETA PRUNING #####################


def heuristic2(board, player):
    score = 0

    quarterHeuristic = [ \
        [50, -5, 20], \
        [-5, -5,  1], \
        [20,  1,  5] \
    ]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                # if len(find_lines(board, i, j, player)) > 0:
                #     score += 2
                # if len(find_lines(board, i, j, player%2 + 1)) > 0:
                #     score -= 2
                continue

            ti = 0
            tj = 0
            if i <= len(board)/2:
                if i < 2:
                    ti = i
                else:
                    ti = 2
            else:
                if i > len(board) - 3:
                    ti = len(board) - i - 1
                else:
                    ti = 2
            
            if j <= len(board[0])/2:
                if j < 2:
                    tj = j
                else:
                    tj = 2
            else:
                if j > len(board[0]) - 3:
                    tj = len(board[0]) - j - 1
                else:
                    tj = 2
  
            if board[i][j] == player:
                score += quarterHeuristic[ti][tj]
            else:
                if quarterHeuristic[ti][tj] == 50:
                    score -= 5*50
                elif quarterHeuristic[ti][tj] == 20:
                    score -= 1.5*20
                else:
                    score -= quarterHeuristic[ti][tj]

    return score


def alphabeta(board, color, depth, maxTime): 
    startTime = time.perf_counter()

    def ab(board, player, maxing, maxDepth, depth = 0, alpha=-1000, beta=1000):

        if depth == maxDepth:
            return heuristic2(board, color), []

        boards = get_possible_moves(board, player)

        if len(boards) == 0: 
            return heuristic2(board, color), []

        if maxing:
            bestScore = -1000
            bestBoard = 0
            bestMove = boards[0]
            for b in boards:
                if time.perf_counter() - startTime>= maxTime:
                    return bestScore, bestMove

                movetoBoard = play_move(board, player, b[0], b[1])

                score, move = ab(movetoBoard, player%2 + 1, False, maxDepth, depth+1, alpha, beta)

                if score > bestScore:
                    bestBoard = movetoBoard
                    bestScore = score
                    bestMove = b
                
                alpha = max(alpha, bestScore)  
  
                # Alpha Beta Pruning  
                if beta <= alpha:  
                    break 
            
            return bestScore, bestMove
        
        else:
            bestScore = 1000
            bestBoard = 0
            bestMove = boards[0]
            for b in boards:
                if time.perf_counter() - startTime>= maxTime:
                    return bestScore, bestMove

                movetoBoard = play_move(board, player, b[0], b[1])

                score, move = ab(movetoBoard, player%2 + 1, True, maxDepth, depth+1, alpha, beta)
                if score < bestScore:
                    bestBoard = movetoBoard
                    bestScore = score
                    bestMove = b
                
                beta = min(beta, bestScore)  
  
                # Alpha Beta Pruning  
                if beta <= alpha:  
                    break 
            
            return bestScore, bestMove
 
    
    score, move = ab(board, color, True, depth)
    

    return move[0], move[1]



####################################################
def run_ai():

    """
    This function establishes communication with the game manager. 
    It first introduces itself and receives its color. 
    Then it repeatedly receives the current score and current board state
    until the game is over. 
    """
    print("Ethan h3") # First line is the name of this AI  
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
            print()
        else: 
            board = eval(input()) # Read in the input and turn it into a Python
                                  # object. The format is a list of rows. The 
                                  # squares in each row are represented by 
                                  # 0 : empty square
                                  # 1 : dark disk (player 1)
                                  # 2 : light disk (player 2)
                    
            movei, movej = alphabeta(board, color, 6, 5)

            print("{} {}".format(movei, movej)) 

if __name__ == "__main__":
    run_ai()
