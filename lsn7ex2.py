import random

number = random.randrange (1,15)

def player_guess ():
    global player_guess_input
    player_guess_input = int(input ('Guess the number from 1 to 15:'))
    error_check()

def error_check():
    if player_guess_input >=16:
        print ('Error. Incert correct number.')
    elif player_guess_input < 1:
        print('Error. Incert correct number.')

def game (number):
    player_guess()
    while number != player_guess_input:
        if player_guess_input > number:
            print('Number is lower.')
            player_guess()
        elif player_guess_input < number:
            print ( 'Number is higher.')
            player_guess()
    else:
        print ( "You won!")


# roll the things

game (number)