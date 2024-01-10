#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Conditionals - testing if strings test true"""

ipchk = input("Apply an IP address: ") # this line now prompts the user for input

# a provided string will test true
if ipchk == "192.168.71.1":
   print("Looks like the IP addres the Gateway was set: " + ipchk + " This is not recommended.") # indented under if
elif ipchk: # returns the following if there is any input at all
    print("Looks like the IP address was set: " + ipchk)
else:    # if data is NOT provided
    print("You did not provide input.") # must be indented under else:
