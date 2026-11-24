#!/usr/bin/python3
"""Displays the value of the X-Request-Id header of a response."""
import requests
import sys

if __name__ == "__main__":
    print(requests.get(sys.argv[1]).headers.get("X-Request-Id"))
