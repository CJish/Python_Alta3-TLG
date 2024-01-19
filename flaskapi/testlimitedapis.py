#!/usr/bin/env python3

import time, requests

URL = 'http://0.0.0.0:2224'

def main():
    start_time = time.time()
    while True:
        get_request = requests.get(f'{URL}/fast')
        if get_request.status_code != 200:
            end_time = time.time()
            break
    print(f'It took {end_time - start_time} seconds to reach the limit')

if __name__ == "__main__":
    main()
