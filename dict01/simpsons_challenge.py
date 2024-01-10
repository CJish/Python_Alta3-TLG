#!/usr/bin/env python3

def challenge_level():
    challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]
    eyes = challenge[2][1]
    goggles = challenge[2][0]
    nothing = challenge[3]
    print(f"My {eyes}! The {goggles} do {nothing}!")
    
def trial_level():
    trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]
    eyes = trial[2].get("goggles")
    goggles = trial[2].get("eyes")
    nothing = trial[3]
    print(f"My {eyes}! The {goggles} do {nothing}!")
    
def nightmare_level():
    nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]
    eyes = nightmare[0].get("user").get("name").get("first")
    goggles = nightmare[0].get("kumquat")
    nothing = nightmare[0].get("d")
    print(f"My {eyes}! The {goggles} do {nothing}!")
    
def main():
    challenge_level()
    trial_level()
    nightmare_level()

main()    
