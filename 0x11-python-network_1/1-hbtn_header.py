#!/usr/bin/python3
"""A script that:
-script that use the package urllib and sys.
-fetches url and show body of the response.
"""
import sys
import urllib.request

if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(request) as response:
        print(response.get("X-Request-Id"))
