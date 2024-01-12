#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
    Conditionals - Life of Brian guessing game without a 'while True' loop."""

round = 0
answer = " "

while round < 3 and answer != "Brian":
    round += 1  # increase the round counter by 1
    answer = input('Finish the movie title: "Monty Python\'s The Life of ______"\n')
    answer = answer.lower()
    if answer == 'Brian':  # the correct answer
        print('Correct!!')
        break
    if answer == 'shrubbery':
        print('You found the super secret answer!')
        break
    elif round == 3: # 3 tries starting at 0
        print('Sorry, the answer was Brian.')
        break
    else:   # if all three answers were wrong
        print('Sorry, try again')
        
