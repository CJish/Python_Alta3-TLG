#!/usr/bin/env python3

import csv

def main():

    with open('superbirthday.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                # above is the python 3.6+ way to do things
                print('Column names are {}'.format(", ".join(row)))
                line_count += 1
            else:
                # print(f'\t{row[0]} aka {row[1]}, was born in {row[2]}.')
                # above is python 3.6+
                print('\t{} aka {}, was born in {}.'.format(row[0],row[1],row[2]))
                line_count += 1
            print(f'Processed {line_count} lines.')

if __name__ == "__main__":
    main()
