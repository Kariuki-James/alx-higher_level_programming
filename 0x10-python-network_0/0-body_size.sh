#!/bin/bash
# Sends GET request to a URL, and displays the size of the response body.
curl -sI "$1" | grep -m 1 -i "content-length" | awk '{ print $2 }'
