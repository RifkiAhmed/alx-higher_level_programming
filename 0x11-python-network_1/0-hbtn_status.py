#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    import urllib.request
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        content = response.read()
        content_type = response.headers.get_content_charset()
        print("Body response:")
        print("    - type:", type(content))
        print("    - content:", content)
        print(f"    - {content_type} content:", content.decode(content_type))
