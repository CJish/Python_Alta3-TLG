#!/usr/bin/env python3

# create a list with three values
my_list = ['192.168.0.5', 5060, "UP"]

# pull the first item from a list and print it
print("The first item in the list (IP): " + my_list[0] )

# pull the second item, convert it to a string, and print it
print("The second item in the list (port): " + str(my_list[1]) )

# pull the third item and print it
print("The third item in the list (state): " + my_list[2] )

iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

# display only the IP addresses from iplist
print(f"IP addresses: {iplist[3]} and {iplist[4]}")

