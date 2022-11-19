#!/usr/bin/python3
"""
- Displays the X-Request-Id header variable of a request to a given URL
- You must use the packages requests and sys
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    x = r.status_code
    if x >= 400:
        print(f"Error code: {x}")
    else:
        print(r.text)
