#!/usr/bin/env python3
hostname = input("What value should we set for hostname?")
## Notice how the next line has changed
## here we use the str.lower() method to return a lowercase string
if hostname.lower() == "mtg":
    # these will print only when the if condition is true
    print("The hostname was found to be mtg\n")
    print("hostname matches expected config\n")

# this always prints
print("Exiting the program\n\n")

