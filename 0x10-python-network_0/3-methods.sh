#!/bin/bash
# Takes in a URL as first arg, and displays all HTTP methods allowed by the server
curl -sI "$1" | grep -m 1 -i "allow" | awk -F': ' '{ print $2 }'
