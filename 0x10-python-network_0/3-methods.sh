#!/bin/bash
# Get all Allow requests methods
curl -sI $1 | grep "Allow" | cut -d ':' -f 2 | xargs
