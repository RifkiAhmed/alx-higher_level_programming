#!/usr/bin/python3
"""
"""
import sys
import urllib.request
import urllib.parse

try:
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.read().decode('utf-8'))
except urllib.error.HTTPError as err:
    print("Error code:", err.status)
