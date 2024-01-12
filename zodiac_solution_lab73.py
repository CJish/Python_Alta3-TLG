#!/usr/bin/env python3
"""TELLS SOMETHING ABOUT YOU BASED ON BIRTH YEAR"""


def main():
    """THE MAIN (AND ONLY) FUNCTION"""
    usr_name = input("Please enter your name:\n>")
    usr_date = int(input("Please enter your birth year in YYYY format, e.g 2010:\n>"))
    dict_key = usr_date % 12
    quotes_dict = {0:["Monkey", "sharp, smart, curious, and mischievious"],
                   1:["Rooster", "hardworking, resourceful, courageous, and talented"],
                   2:["Dog", "loyal, honest, cautious, and kind"],
                   3:["Pig", "a symbol of wealth, honesty, and practicality"],
                   4:["Rat", "artistic, sociable, industrious, charming, and intelligent"],
                   5:["Ox", "strong, thorough, determined, loyal, and reliable"],
                   6:["Tiger", "courageous, enthusiastic, confident, charismatic, and a leader"],
                   7:["Rabbit", "vigilant, witty, quick-minded, and ingenious"],
                   8:["Dragon", "talented, powerful, lucky, and successful"],
                   9:["Snake", "wise, like to work alone, and determined"],
                   10:["Horse", "animated, active, and energetic"],
                   11:["Sheep", "creative, resilient, gentle, mild-mannered, and shy"]}
    sign = quotes_dict[dict_key][0]
    attributes = quotes_dict[dict_key][1]
    print(f'{usr_name}, your zodiac sign is {sign}. You are {attributes}.')

main()
