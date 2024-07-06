#!/bin/bash
# Sends a request to the URL passed as an argument and displays the size of the body of the response in bytes
curl -s -o /dev/null -w "%{size_download}\n" "$1"
