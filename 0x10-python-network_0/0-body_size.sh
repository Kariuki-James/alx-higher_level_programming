#!/usr/bin/env bash
# sends a request to a URL, and displays the size of the response body.

if [[ $# -lt 1 ]]; then
    echo "Error: No URL provided."
    echo "Usage: ./0-body_size.sh <URL>"
    exit 1
fi

response_header=$(curl -sI "$1")
content_length=$(echo "$response_header" | grep -m 1 -i "content-length" | awk '{ print $2 }')
echo "$content_length"
