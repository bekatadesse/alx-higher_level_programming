#!/usr/bin/python3
"""A script that:
-script that use the package urllib and sys.
-fetches url and show body of the response.
"""

import sys
import urllib.request


url = sys.argv[1]
request = urllib.request.Request(url)
with urllib.request.urlopen(request) as response:
    print(dict(response.headers).get("X-Request-Id"))
