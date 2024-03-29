#!/usr/bin/env python3

# from python std library
import csv

# python3 -m pip install np
import numpy as np
# python3 -m pip install matplotlib
import matplotlib
matplotlib.use('Agg')
# sudo apt install python3-tk
import matplotlib.pyplot as plt

def parsecsvdata():
    """returns a list. [0] is LAN and [1] WAN data"""
    summary = [] # list that will contain [(LAN), (WAN)]

    # open csv data 
    with open('/home/student/mycode/graphing/2018summary.csv',\
            "r") as downtime:
        # parse csv data with csv.reader
        downdata = csv.reader(downtime, delimiter = ',')
        for row in downdata:
            rowdat = (int(row[0]), int(row[1]), int(row[2]), int(row[3]))
            summary.append(rowdat) # add dict to list
    return summary

def main():
    N = 4
    # grab our data
    summary = parsecsvdata()
    # LAN data
    localnetMeans = summary[0]
    # WAN data
    wanMeans = summary[1]

    # x locations for the groups
    ind = np.arange(N)
    # the width of the bars: can also be 0.35
    width = len(summary)

    # describe where to display p1
    p1 = plt.bar(ind, localnetMeans, width)
    # stack p2 on top of p1
    p2 = plt.bar(ind, wanMeans, width, bottom=localnetMeans)

    # Describe the table metadata
    plt.ylabel("Length of Outage (mins)")
    plt.title("2018 Network Summary")
    plt.xticks(ind, ("Q1", "Q2", "Q3", "Q4"))
    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0]), ("LAN", "WAN"))

    # SAVE the graph locally
    plt.savefig("/home/student/mycode/graphing/2018summaryv2.png")
    # Save to "~/static"
    plt.savefig("/home/student/static/2018summaryv2.png")
    print("Graph created.")

if __name__ == "__main__":
    main()
