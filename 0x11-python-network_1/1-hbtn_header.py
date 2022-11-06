#!/usr/bin/python3
"""A script that:
-script that use the package urllib and sys.
-fetches url and show body of the response.
"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        print(html.get('X-Request-Id'))
