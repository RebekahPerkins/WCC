import random

def get_guess():

    guess = raw_input('Enter your guess: ')

    valid = False

    while valid != True:

        try:
            guess = int(guess)
        except Exception:
            print('Invalid input; please enter a whole number.')
            valid = False
            guess = get_guess()

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
    max_guess = 5

    print('\nI\'m thinking of a number between ' + str(lowNum) + ' and ' + str(highNum) + ', what do you think it is?')
    
    guess = int(get_guess())
    
    for guess_count in range(1,6):
        if guess == secret_number:
            print('You got it! Secret number was ' + str(secret_number) + '.')
            if 1 == guess_count:
                print('It took you 1 guess.')
            else:
                print('It took you ' + str(guess_count) + ' guesses.')
            break
        if guess_count == 5:
            print('Sorry, you lose. The number was ' + str(secret_number) + '.')
            break
        print('Too ' + compare(guess, secret_number) + '. Guess again.')
        print('You have ' + str(max_guess - guess_count) + ' guesses left.')
        guess = int(get_guess())
        
play(1,50)