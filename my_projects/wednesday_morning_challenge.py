#!usr/bin/env python3

# Ask user for name, age, and fav movie
# store this in a list
# return in clean, readable format
# capitalize name and movie, age should be integer

# use a function for the code

# ask what genre the movie is and the name of one actor

# store the movie title, actor, and genre in an internal list (without returning it)

def main():
    user_input()
    more_questions()


def user_input():
    user_name = input("What's your name?")
    user_name = user_name.capitalize()
    user_age = input(f"Hey, {user_name}, how old are you?")
    user_fav_movie = input(f"Last question, {user_name}: what's your favorite movie?")
    user_inputlist = [user_name, user_age, user_fav_movie]
    print("Let me make sure I got this right:")
    print(f"Your name is {user_inputlist[0]}, you're {user_inputlist[1]} years old, and your favorite movie is {user_inputlist[2]}.")

def more_questions():
    more_q = input("Actually, do you mind if I ask a few more questions? y to continue")
    if (more_q == "y"):
        print("Sweet, thanks")
        print("So you seem to like {user_inputlist[2]}")
        genre = input("What genre would you say {user_inputlist[2]} falls under?")
        actor = input("And tell me one actor who appears in {user_inputlist[2]}.")
        print(f"Awesome, thanks so much {user_inputlist[0]}")

main()
