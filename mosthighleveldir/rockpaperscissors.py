import random


# Parameters: a String `move`
# Returns: Boolean for whether move is valid
#
# Valid moves include 'rock', 'paper', or 'scissors'`
#
def check_move(move):
    return move == 'rock' or move == 'scissors' or move == 'paper'
    
# Parameters: None
# Returns: String of 'rock', 'paper', or scissors'
# Prompts the user for a move
# Makes sure that move is valid; if it's not, continues to ask user for a move
def get_player_move():

    # Prompt the user to enter their move
    move = raw_input('Pick your move: rock, paper, or scissors? ')

    # This will happen on a loop until the user enters a valid move
    while check_move(move) == False:
        print('Invalid move; pick again.')
        # Run this function again, so they're asked to enter a new move
        move = get_player_move()

    # If they get out of the while loop, it means they
    # entered a valid move, so return it
    return move

# Parameters: None
# Returns: String of 'rock', 'paper', or 'scissors'
def get_computer_move():
    moves = ['rock', 'paper', 'scissors'];
    return random.choice(moves)

# Parameters: String moveA, String moveB
# Returns: Boolean if moveA beats moveB according to the rules of RPS
#
# Examples:
# If moveA is 'rock' and moveB is 'paper', it should return False
# If moveA is 'paper' and moveB is 'rock', it should return True
#
# Should work for 6 different possible combinations of moveA and moveB
# Will not be concerned with ties; i.e, moveA will never be the same as moveB
def judge(moveA, moveB):
    aWins = False
    if moveA == 'rock' and moveB == 'scissors':
        aWins = True
    elif moveA == 'scissors' and moveB == 'paper':
        aWins = True
    elif moveA == 'paper' and moveB == 'rock':
        aWins = True
    return aWins

def play():

    print('Welcome to Welcome to Rock, Paper, Scissors!')

    # Player goes
    player_move = get_player_move()

    # Computer goes
    computer_move = get_computer_move()
    print('The computer picked: ' + computer_move)

    # Figure out who won
    # Print results; either: `Tie`, `You Won!`, or `The computer won.`
    if judge(player_move, computer_move):
        print("You Won!")
    elif judge(computer_move, player_move):
        print("The computer won.")
    else:
        print('Tie')

    # Prompt to play again
    play_again = raw_input('Play again? Type `y` or `n`: ')

    if(play_again == 'y'):
        play()
    else:
        print('Thanks for playing!')

# Run the game
play()