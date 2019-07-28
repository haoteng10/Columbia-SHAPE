To run othello:

Try (in a terminal):
        python othello_gui.py

or in spyder: "run othello_gui.py"

This should open a window that generates a board.

To change the dimension of the board, look for the line near the bottom:
   game = OthelloGameManager(dimension=8)

You can change the dimension of the board (e..g, to a smaller board of 4)


Without parameters, the game has 2 human players.  The parameters can be used to indicate opponents.  There is an existing opponent code, randy_ai.py that plays a random player so:

python othello_gui.py randy_ai.py  <- you play against random 
python othello_gui.py randy_ai.py  randy_ai.py <- 2 randoms play against each other

