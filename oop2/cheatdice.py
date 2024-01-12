#!/usr/bin/python3
"""RZFeeser | Alta3 Research
   Player - Class model
   Cheat_Swapper(Player) - Subclass model
   Cheat_Loaded_Dice(Player) - Subclass model"""

# standard library
from random import randint

class Player:
    def __init__(self):
        self.dice = []

    def roll(self):
        self.dice = [] # clears current dice
        for i in range(3):  # make 3 rolls
            self.dice.append(randint(1,6))   # 1 to 6 inclusive

    def get_dice(self): # returns the dice rolls
        return self.dice

# allows user to turn their last roll into a 6
class Cheat_Swapper(Player):  # inheritance of Player
    def cheat(self):
        self.dice[-1] = 6

# allows user to increase all rolls if they were less than a 6
class Cheat_Loaded_Dice(Player): # inheritance of Player
    def cheat(self):
        i = 0
        while i < len(self.dice):
            if self.dice[i] < 6:
                self.dice[i] += 1
            i += 1
class Cheat_Mulligan(Player): # inheritance of Player
    def cheat(self):
        if self.dice[0] < 3:
            self.dice[0] = random.randint(0,6) # replaces the first roll with a new roll

class Cheat_ExtraDice(Player): # inheritance 
    def cheat(self):
        self.dice.append(random.randint(0,6) # throws one extra roll

class Cheat_WeightedDice(Player): # inheritance of Player
    def cheat(self):
        for i in self.dice[]:
            if self.dice[i] < 2: # if the roll is less than 2
                self.dice[i] = random.randint(1,6) # roll with a minimum number of 1

class Cheat_Sabotage(Player) # inherets from Player


