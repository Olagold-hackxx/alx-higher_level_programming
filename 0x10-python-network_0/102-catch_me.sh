#!/bin/bash
#makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message  You got me!,
curl -sX PUT -d "user_id=98" -H "origin: School" -L 0.0.0.0:5000/catch_me_3
