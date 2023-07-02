#!/bin/bash
# Takes in a URL as first arg, sends GET request, and displays the response body.
curl -s -H "X-School-User-Id: 98" "$1"
