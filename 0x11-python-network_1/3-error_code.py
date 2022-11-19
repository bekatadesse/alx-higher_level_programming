#!/usr/bin/python3
"""
- sends a request to the URL and
- displays the body of the response
"""
from urllib import request, error
import sys

try:
    with request.urlopen(sys.argv[1]) as respons:
        print(respons.read().decode('UTF-8'))
except error.HTTPError as e:
    # print(e.code)
    # print(e.read())
