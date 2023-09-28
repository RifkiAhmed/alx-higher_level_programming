#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
(curl -si -o /dev/null "$1" | grep -q "200") && curl -s "$1"
