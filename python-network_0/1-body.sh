#!/bin/bash
# Sends a GET request to a URL, follows redirects, and displays the body only for a 200 status code
curl -sfL "$1"
