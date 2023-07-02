#!/bin/bash
# Takes in a URL as first arg, sends a request, and displays only the status code of response
curl -s -o /dev/null -w "%{http_code}" "$1"
