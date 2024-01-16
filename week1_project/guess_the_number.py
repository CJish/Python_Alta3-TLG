#!/usr/bin/env python3

"""GUESS THE NUMBER GAME"""
"""created by CJish"""

import random
import os

def get_range_and_tries(): # sets the min/max of the range, returns min/max & number of tries
    while True:
        try:
            num1 = int(input('Enter the first number: '))
            num2 = int(input('Enter the second number: '))
            num3 = int(input('How many tries do you want? '))
        except ValueError:
            print("That's not a whole number.")
            print("Let's try again")
            continue
        else:
            if num1 > num2:
                max_bound = num1
                min_bound = num2
                break
            else:
                max_bound = num2
                min_bound = num1
                break
    return min_bound, max_bound, num3

def gen_answer(a, b): # takes min/max (a/b) and uses those to return a random int in that range
    print(f'I\'m going to choose a number between {a} and {b}.')
    return random.randint(a, b)

def make_guess(a,b,c): # inputs the user's guess. checks guess against range, increments counter. returns guess & counter
    print('\nPlease guess a number')
    guess = input()
    c += 1
    try:
        guess = int(guess)
        print('')
        return guess, c
    except:
        print(f'Your guess of "{guess}" was not a whole number\nPlease fix your guess to be a whole number between {a} and {b}.')
        return make_guess(a,b,c)

def you_win(a, b): # called when user wins. Asks if user wants to play again
    if a == 1:
        print('You got it on your first try!')
        print('That\'s amazing!!!!!!!!!!!!!!!')
        play_again()
    elif a == b:
        print('You must be great under pressure: ')
        print('YOU GOT IT ON YOUR LAST TRY!')
        play_again()
    else:
        print('Great job!')
        print(f'You guessed the number in {a} tries!')
        play_again()

def invalid_guess(a,b,c): # handles invalid guesses
    print(f'You guessed "{c}".')
    print(f'Your guess must be between {a} and {b}')

def play_again(): # handles restarting the game if the user desires
    print('Do you want to play again?  y or n')
    play_yn = input()
    if play_yn == 'y':
        clear = lambda: os.system('clear')
        clear()
        # print("\n" * 100) # this is left over from IDLE
        main()
    else:
        exit()

# move the beginning of main() into an intro function

def main():
    counter = 0
    guess = ''
    name = input('Hello. What is your name?')
    print(f'Well, {name}, We\'re going to play a guessing game')
    print('You\'re going to tell me two numbers,')
    print('and I\'ll pick one within that range.')
    print('Then you\'ll guess that number.')
    min_bound, max_bound, num_tries = get_range_and_tries()
    answer = gen_answer(min_bound, max_bound)
    print(f'You have {num_tries} tries to guess the number.')
    while guess != answer:
        guess, counter = make_guess(min_bound, max_bound, counter)
        if guess == answer:
            you_win(counter, num_tries)
        if counter >= num_tries:
            print(f'You\'ve reached your limit of {num_tries}.')
            print(f'Sorry, {name}, you\'ll have to try again.')
            print(':(       <--that\'s a sad face \n')
            play_again()
        try:
            if guess < min_bound or guess > max_bound:
                invalid_guess(min_bound, max_bound, guess)
            elif guess < answer:
                print(f'Your guess is too low')
            elif guess > answer:
                print(f'Your guess is too high')
        except:
            print('We seem to have an error, but I don\'nt know what it is.')
            continue

if __name__ == "__main__":
    main()
