#!/bin/bash
# curl and filter
curl -I "$1" -s | grep Content-Length | cut -d ' ' -f2
