#!/usr/bin/env python3

import csv

def main():
    with open('inventory.csv', mode = 'w') as csv_file:
        fieldnames = ['hostname', 'ip', 'service']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'hostname':'dumbledore', 'ip': '10.0.2.66', 'service': 'httpd'})


if __name__ == "__main__":
    main()
