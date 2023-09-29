#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    content = response.read()
    content_type = response.headers.get_content_charset()
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
    print(f"\t- {content_type} content:", content.decode(content_type))
