#!/usr/bin/python3
"""A script that:
-script that use the package urllib and sys.
-fetches url and show body of the response.
"""
import urllib.request
import sys


if __name__ == "__main__":
    resp = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(resp) as response:
        html = response.info()
        print(html.get('X-Request-Id'))
