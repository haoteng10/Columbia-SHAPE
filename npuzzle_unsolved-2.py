"""
SHAPE'19

In this assignment you will implement and compare different search strategies
for solving the n-Puzzle, which is a generalization of the 8 and 15 puzzle to
squares of arbitrary size (we will only test it with 8-puzzles for now). 
See Courseworks for detailed instructions.

"""

import time

def state_to_string(state):
    row_strings = [" ".join([str(cell) for cell in row]) for row in state]
    x = "\n".join(row_strings)
    x = x.replace("0", " ")
    return x

def swap_cells(state, i1, j1, i2, j2):
    """
    Returns a new state with the cells (i1,j1) and (i2,j2) swapped. 
    """
    value1 = state[i1][j1]
    value2 = state[i2][j2]
    
    new_state = []
    for row in range(len(state)): 
        new_row = []
        for column in range(len(state[row])): 
            if row == i1 and column == j1: 
                new_row.append(value2)
            elif row == i2 and column == j2:
                new_row.append(value1)
            else: 
                new_row.append(state[row][column])
        new_state.append(tuple(new_row))
    return tuple(new_state)
    

def get_successors(state):
    """
    This function returns a list of possible successor states resulting
    from applicable actions. 
    The result should be a list containing (Action, state) tuples. 
    For example [("Up", ((1, 4, 2),(0, 5, 8),(3, 6, 7))), 
                 ("Left",((4, 0, 2),(1, 5, 8),(3, 6, 7)))] 
    """ 
    child_states = []

    for row in range(len(state)):
        for column in range(len(state[row])):
            if state[row][column] == 0:
                if column < len(state)-1: # Left 
                    new_state = swap_cells(state, row,column, row, column+1)
                    child_states.append(("Left",new_state))
                if column > 0: # Right 
                    new_state = swap_cells(state, row,column, row, column-1)
                    child_states.append(("Right",new_state))
                if row < len(state)-1:   #Up 
                    new_state = swap_cells(state, row,column, row+1, column)
                    child_states.append(("Up",new_state))
                if row > 0: # Down
                    new_state = swap_cells(state, row,column, row-1, column)
                    child_states.append(("Down", new_state))
                break
    return child_states

            
def goal_test(state):
    """
    Returns True if the state is a goal state, False otherwise. 
    """    
    counter = 0
    for row in state:
        for cell in row: 
            if counter != cell: 
                return False 
            counter += 1
    return True
   
def bfs(state):
    """
    Breadth first search.
    Returns three values: A list of actions, the number of states expanded, and
    the maximum size of the frontier.  
    """
    FIFO_queue = []
    parents = []
    actions = {}
    costs = {}

    costs[state] = 0

    visited = list()
    # Write code here for bfs.
    
    
                
    #Check if there is a number around it....if so...record it...
    
    #Check Top
    #if (state[start_vertex[0]-1][start_vertex[1]] in possibleNo):
#    if(state[start_vertex[0]-1][start_vertex[1]] != state[2][start_vertex[1]]):
#        canMove["UP"] = True
    #Check Downstart_vertex = [0,0]
#    canMove = {
#            "UP": False,
#            "DOWN": False,
#            "LEFT": False,
#            "RIGHT": False
#            }
#    
#    print(state[0])
#    print(state[1])
#    print(state[2])
#
#    
#    possibleNo = [1,2,3,4,5,6,7,8]
#            
#    for row_i in range(3):
#        for item_i in range(3):
#            print (state[row_i][item_i])
#            if(state[row_i][item_i] == 0):
#                start_vertex[0] = row_i
#                start_vertex[1] = item_i
#    if (state[start_vertex[0]+1][start_vertex[1]] in possibleNo):
#        canMove["DOWN"] = True
#    #Check Left
#    #if (state[start_vertex[0]][start_vertex[1]-1] in possibleNo):
#    if(state[start_vertex[0]][start_vertex[1]-1] != state[start_vertex[0]][2]):
#        print("Weird No. " + str(state[start_vertex[0]][start_vertex[1]-1]))
#        canMove["LEFT"] = True
#    #Check Right
#    if (state[start_vertex[0]][start_vertex[1]+1] in possibleNo):
#        canMove["RIGHT"] = True
    
    #print(start_vertex)
    #print(canMove)
    
    counter = int(0)
    parent_counter = 1
    solved = False
    successors = []

    visited.append(state)

    firstState = ('None', (state))

    FIFO_queue.append(firstState)
    if (goal_test(state)):
        return actions
    else:

        successors = get_successors(state)
        for successor in successors:
            #FIFO_queue.append(successor[1:][0])
            FIFO_queue.append(successor)
            #print(FIFO_queue)

        while(solved != True):

            for i in range(len(successors)):

                #print(FIFO_queue[counter][0:])
                print(FIFO_queue[counter][0:][0])
                if(goal_test(FIFO_queue[counter][1:][0])):
                    #actions.add(successors[])
                    solved = True
                    return parents
                counter += 1
                #print(counter)
                #print(FIFO_queue[counter])

            successors = get_successors(FIFO_queue[parent_counter][1:][0])
            parent_counter += 1
            parents.append(FIFO_queue[parent_counter][0:][0])

            for successor in successors:
                #FIFO_queue.append(successor[1:][0])
                FIFO_queue.append(successor)
                #print(successor)
                #successor_action[successor[:1]] = successor[1:]

            #print(FIFO_queue)
                
                
    return None# No solution found
                               
#No. of tiles in correct position
#Avg. distance

def dfs(state):
    """
    Depth first search.
    Returns three values: A list of actions, the number of states expanded, and
    the maximum size of the frontier.  
    """
    Stack = []
    parents = {}
    actions = {}
    costs = {}

    costs[state] = 0

    #Write code here for dfs  
                
    return None # No solution found


def misplaced_heuristic(state):
    """
    Returns the number of misplaced tiles.
    """
    return 0 # replace this


def manhattan_heuristic(state):
    """
    For each misplaced tile, compute the manhattan distance between the current
    position and the goal position. THen sum all distances. 
    """

    return 0 # replace this


def get_solution(state, parents, actions, costs):
    """
    Helper function to retrieve the solution. This was not part of the
    provided scaffolding.
    """

    # Write solution traversal here

    return []


def best_first(state, heuristic = misplaced_heuristic):
    """
    Breadth first search using the heuristic function passed as a parameter.
    Returns three values: A list of actions, the number of states expanded, and
    the maximum size of the frontier.  
    """

    # You might want to use these functions to maintain a priority queue
    # You may also use your own heap class here
    from heapq import heappush
    from heapq import heappop

    parents = {}
    actions = {}
    costs = {}

    costs[state] = 0

    # Write best first search here.

    return None # No solution found


def astar(state, heuristic = misplaced_heuristic):
    """
    A-star search using the heuristic function passed as a parameter. 
    Returns three values: A list of actions, the number of states expanded, and
    the maximum size of the frontier.  
    """
    # You might want to use these functions to maintain a priority queue
    # You may also use your own heap class here

    from heapq import heappush
    from heapq import heappop

    parents = {}
    actions = {}
    costs = {}

    costs[state] = 0
    
    # Write A* search here

    return None # No solution found


def print_result(solution):
    """
    Helper function to format test output. 
    """
    if solution is None: 
        print("No solution found.")
    else: 
        print("Solution has {} actions.".format(len(solution)))



if __name__ == "__main__":

    #Easy test case
    test_state = ((1, 4, 2),
                  (0, 5, 8), 
                  (3, 6, 7))  

    #More difficult test case
    #test_state = ((7, 2, 4),
    #              (5, 0, 6), 
    #              (8, 3, 1))  

    print(state_to_string(test_state))
    print()

    print("====BFS====")
    start = time.time()
    solution = bfs(test_state) #
    print_result(solution)
    end = time.time()
    if solution is not None:
        print(solution)
    print("Total time: {0:.3f}s".format(end-start))

    print() 
    print("====DFS====") 
    start = time.time()
    solution = dfs(test_state)
    end = time.time()
    print_result(solution)
    print("Total time: {0:.3f}s".format(end-start))


    print() 
    print("====Greedy DFS====") 
    start = time.time()
    solution = best_first(test_state, misplaced_heuristic)
    end = time.time()
    print_result(solution)
    print("Total time: {0:.3f}s".format(end-start))
    

    print() 
    print("====Best-First====") 
    start = time.time()
    solution = best_first(test_state, misplaced_heuristic)
    end = time.time()
    print_result(solution)
    print("Total time: {0:.3f}s".format(end-start))
    
    print() 
    print("====A* (Misplaced Tiles Heuristic)====") 
    start = time.time()
    solution = astar(test_state, misplaced_heuristic)
    end = time.time()
    print_result(solution)
    print("Total time: {0:.3f}s".format(end-start))


