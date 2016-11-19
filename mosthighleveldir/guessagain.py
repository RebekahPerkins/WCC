import random

# Get the user's guess
# Params: None
# Returns: Integer
#
def get_guess():

    # Get initial guess
    guess = raw_input('Enter your guess: ')

    # Assume it's not valid, until it's proven otherwise
    valid = False

    while valid != True:

        try:
            # Try and convert this number to an integer
            # If it fails, the exception will occur
            guess = int(guess)
        except Exception:
            # Exception was thrown when trying to convert to number,
            # Report the issue and ask again
            print('Invalid input; please enter a whole number.')
            valid = False
            guess = get_guess()

        # If they get here, it means the number must have been valid
        # Set valid to be true to break out of the while loop
        valid = True

    return guess


def compare(numA, numB):
    if numA > numB:
        return 'high'
    elif numB > numA:
        return 'low'

# main function
# Param: low and high limits
# Returns: String result
def play(lowNum, highNum):
    secret_number = random.randint(lowNum, highNum)
    
    print('number is ' + str(secret_number))
    
    print('\nI\'m thinking of a number between ' + str(lowNum) + ' and ' + str(highNum) + ', what do you think it is?')
    
    guess = int(get_guess())
    count = 1
    while guess != secret_number:
        print('Too ' + compare(guess, secret_number) + '. Guess again.')
        guess = int(get_guess())
        count = count + 1
    print('You got it! Secret number was ' + str(secret_number))
    print('It took you ' + str(count) + ' guesses.')
    
play(1,10)