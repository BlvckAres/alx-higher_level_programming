#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""
from sys import argv
from urllib.request import Request, urlopen

if __name__ == "__main__":
    req = request.Request(argv[1])
    with request.urlopen(req) as response:
        body = str(response.info())
        if "X-Request-Id: " in body:
            body = body.split("X-Request-Id: ")[1]
            answer = body.split('\n')[0]
            print(answer)
