import time

import requests


def main():
    while True:
        time.sleep(12)
        requests.put('http://backend:8000/PersonLocationsUpdate/')


if __name__ == '__main__':
    main()
