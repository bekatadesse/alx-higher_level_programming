#!/usr/bin/python3
"""
script that use the package urllib and fetches url
and show body of the response
"""
import urllib.request
response = urllib.request.Request('https://alx-intranet.hbtn.io/status')
response = urllib.request.urlopen(response)
resp = response.read()

print('Body response:')
print(f"\t- type: {type(resp)}")
print(f"\t- content: {resp}")
print(f"\t- utf8 content: {resp.decode('utf-8')}")
