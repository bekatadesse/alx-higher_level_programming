#!/usr/bin/python3
"""
script that use the package urllib and sys and fetches url
and show body of the response
"""
import urllib.request
import sys
url = sys.argv[1]
request = urllib.request.Request(url)
with urllib.request.urlopen(request) as response:
    print(dict(response.headers).get("X-Request-Id"))
