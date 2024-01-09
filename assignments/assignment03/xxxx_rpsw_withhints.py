##########################################################################
# INSERT YOUR NAME AND ITU EMAIL ADDRESS HERE:
# NAME: ""
# ITU EMAIL ADDRESS: ""

##########################################################################
# IMPORTING MODULES
# import the random module needed
import random
# "seed" the random module with 42
random.seed(42)

##########################################################################
# DEFINING FUNCTIONS

# define a function that: 
# with the string "Rock, paper, scissors, worldpeace, or quit? (R, P, S, W, Q) ",
# prompts the user to input a letter;
# converts the user input into upper case by default;
# checks whether user input is an accepted value (R, P, S, W, or Q);
# and if not - keeps on asking the same question until input is an accepted value;
# finally, function returns the user input (in upper case)
def user_plays():
    raise NotImplementedError()
    # get input from user    
    # convert into uppercase

    # check if user_move is a valid input;
    # while it is not, keep on asking 
    # (repeat same 2 steps from above, as long as needed)

    # return a valid user move

# define a function for the move made by the computer:
# each time the computer plays, randomly choose and return R/P/S 
# (computer will never want to quit, and never play worldpeace)
def computer_plays():
    raise NotImplementedError()

# define a function that evaluate two moves (both either R, P, or S)
# against each other and returns a string containing both moves and either 
# "you win", "computer wins", or "it's a tie"
def evaluate_moves(usermove, computermove):
    raise NotImplementedError()
    # if... (either it's a tie)
    # elif... (or you won)
    # else... (or, in all other cases, you lose)

##########################################################################
# GAME STARTS

# Welcome message

# eternal while loop

    # let user make a move (R, P, S, W, or Q) with the user_plays() function
    
    # if user wants to quit, break out of the while loop

    # if user inputs "W" (or "w"), they immediately win

    # else, we play a proper round of rock paper scissors: 
        # computer makes a move with the computer_plays() function,        
        # the moves are evaluated against each other with the evaluate_moves() function,
        # (we only have to consider the cases R, P, S for each)
        # show the result to the user