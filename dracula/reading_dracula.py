#!/usr/bin/env python3

with open("dracula.txt", "r") as dracula_object:
    counter = 0
    with open("vampytimes.txt", "w") as vampire_times:
        # for eachline in dracula_object: # this will iterate over each line and print it out
        #     print(eachline)             # 
        for eachline in dracula_object:
            # if eachline.find("vampire") != -1:  # this works, but....
            #     print(eachline)
            if "vampire" in eachline.lower():
                print(eachline)
                vampire_times.write(eachline)
                counter += 1

print(counter)


