#!/usr/bin/env python3

import requests

# define the URL

ISS_URL = 'http://api.open-notify.org/iss-now.json'

def main():

    # call the api
    ISS_JSON = requests.get(ISS_URL)

    # strip off the JSON and return a Python dictionary
    py_iss = ISS_JSON.json()

    iss_lat = py_iss['iss_position']['latitude']
    iss_long = py_iss['iss_position']['longitude']

    print('The current location of the ISS is: ')
    print(f'Lat: {iss_lat}')
    print(f'Long: {iss_long}')


if __name__ == "__main__":
    main()
