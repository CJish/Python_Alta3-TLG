#!/usr/bin/env python3

import pandas as pd

def main():
    opsd_daily = pd.read_csv('netTraffic.csv') # this opens the csv dataset
    
    print('opsd_daily.shape')
    print(opsd_daily.shape)
    # (4383, 5) 
    # our data has 4383 rows covering 1 Jan 2006 - 31 Dec 2017

    print('\nLook at the first three rows')
    print(opsd_daily.head(3))

    print('\nLook at the last three rows')
    print(opsd_daily.tail(3))

    # check out the data types of each column
    print('data types')
    print(opsd_daily.dtypes)

    # set the date as the data frame's index
    opsd_daily = opsd_daily.set_index('Date')

    print('\nLook at the first three rows after date has been set as the primary index')
    print(opsd_daily.head(3))

    print('\nLook at the last three rows after date has been set as the primary index')
    print(opsd_daily.tail(3))

    # display all of the index values (this is a lot of data)
    input('\nPress ENTER to look at all of the index values associated with the dataset')
    print(opsd_daily.index)

    # consolidate the above steps into a single line using the index_col and parse_dates paramaeters of the read_csv() function
    opsd_daily = pd.read_csv('netTraffic.csv', index_col = 0, parse_dates = True)

    # add some additional columns to our data
    # add columns with year, month, and weekday name
    opsd_daily['Year'] = opsd_daily.index.year
    opsd_daily['Month'] = opsd_daily.index.month
    # required to 'pull' the day name (e.g. Monday, Tuesday...)
    opsd_daily['Weekday Name'] = opsd_daily.index.day_name()

    # display a random sampling of 5 rowx
    input('\nPress ENTER to look at a random sampling from 5 rows after adding the Year, Month and Weekday name columns')
    print(opsd_daily.sample(5, random_state = 0))

if __name__ == "__main__":
    main()
